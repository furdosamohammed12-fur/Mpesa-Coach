import os
from dotenv import load_dotenv
from google import genai
from google.genai import types
import json
from datetime import datetime

load_dotenv()
api_key=os.getenv("API_KEY")

if api_key:
    print("Hey🙂")
else:
    print("Key lost")
    
client=genai.Client(api_key=api_key)
MODEL_NAME = "gemini-3.5-flash"

# AI instructions
ROLE="You are Pesa Coach, a friendly money coach for young Kenyans."
TASK="The user tells you what they spent, one or two items per message. Put each expense in a category (transport, food, airtime, rent, shopping, other), keep running totals by category, and answer questions about their spending"
CONTEXT="The user is in Kenya and uses Kenyan shillings (KES). This is a conversation over several turns, so use earlier messages when you answer."
CONSTRAINTS="Only talk about the user's spending. Never invent an amount the user did not give you. If an amount is missing, ask for it. Keep every reply under 60 words."
OUTPUT = 'Reply ONLY with valid JSON and nothing else, with no markdown. Use exactly these field names and no others: "reply" (a short friendly message to the user), "total_spent" (a number: total KES spent so far in this conversation), "totals" (an object with each category and its running total, for example {"transport": 200, "food": 150}). Never leave a field empty.'

SYSTEM_PROMPT = ROLE + "\n" + TASK + "\n" + CONTEXT + "\n" + CONSTRAINTS + "\n" + OUTPUT

# --- Summary prompt (RTCCO) --- 
S_ROLE = "You are Pesa Coach, a money coach for young Kenyans, now writing the end-of-session summary."
S_TASK = "Read the whole conversation and summarise the user's spending."
S_CONTEXT = "The conversation is a record of the expenses the user reported in one session. All amounts are in Kenyan shillings (KES)."
S_CONSTRAINTS = "Use only amounts the user gave you. Never invent an expense. Give exactly three ways to save, each practical for someone in Kenya and based on this user's own spending."
S_OUTPUT = 'Reply ONLY with valid JSON and nothing else, with no markdown. Use exactly these field names and no others: "summary" (2 or 3 short sentences), "breakdown" (an object of category and total KES), "total_spent" (a number), "ways_to_save" (a list of exactly three short tips).'
SUMMARY_PROMPT = S_ROLE + "\n" + S_TASK + "\n" + S_CONTEXT + "\n" + S_CONSTRAINTS + "\n" + S_OUTPUT

# --- RAG knowledge base: saving tips the AI can use ---
KNOWLEDGE_BASE = [
    {"keywords": ["matatu", "transport", "fare", "boda", "uber", "bolt"],
     "tip": "Fares often rise at peak hours and when it rains, so travelling a little earlier or later can cost less. Walk short distances when it is safe."},
    {"keywords": ["airtime", "data", "bundle", "safaricom"],
     "tip": "Compare daily, weekly and monthly bundles before buying. A bundle that matches your real use is usually cheaper than many small top-ups."},
    {"keywords": ["food", "lunch", "supper", "breakfast", "groceries"],
     "tip": "Carrying lunch from home a few days a week usually costs less than buying it daily. Buy staples like rice, beans and maize flour in larger packs when you can."},
    {"keywords": ["rent", "house", "landlord"],
     "tip": "Set aside rent as soon as money comes in, so it is not spent on small things during the month."},
    {"keywords": ["mpesa", "m-pesa", "withdraw", "send", "sent", "fee", "charges"],
     "tip": "M-Pesa send and withdrawal charges add up. Check the current charges, and pay through a till or paybill where it is offered, instead of withdrawing cash first."},
    {"keywords": ["save", "saving", "savings", "budget", "salary", "income"],
     "tip": "Treat saving like a bill: move a small fixed amount to a separate savings place on payday, instead of saving whatever is left."},
]