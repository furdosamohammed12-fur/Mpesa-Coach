# Mpesa-Coach
Expense coach
Pesa Coach: How It Works

Pesa Coach is a money coach for young Kenyans. You tell it what you spent, and it helps you understand your spending.

1. The menu
When the program starts, the user sees a menu. They can start a new session, open a past session, or exit.

2. Telling the coach what you spent
In a new session, the user types an expense, for example "I spent 200 on matatu". The coach puts it in a category: transport, food, airtime, rent, shopping, or other. It keeps a running total for each category. The coach remembers the whole conversation, so the user can ask questions like "How much have I spent on food?"

3. The AI
The program sends the message to an AI model called Gemini. We gave Gemini clear instructions: who it is, what its task is, and what rules it must follow. For example, it must never invent an amount, and it must keep replies short. Gemini replies in a fixed format so our program can read it.

4. Checking the answer
The program checks that the reply has everything we asked for. If something is missing, it asks Gemini once more. This makes the system more reliable.

5. Saving tips (knowledge base)
We wrote a small list of saving tips for Kenya, for transport, food, airtime, rent, and M-Pesa charges. When the user mentions one of these topics, the program finds the matching tip and gives it to Gemini. Gemini uses these real tips instead of inventing its own.

6. When the internet fails
If the AI cannot be reached, the program uses the last saved totals to answer. It cannot record new expenses while offline.

7. The summary
When the user types "exit", the AI reads the whole conversation. It writes a short summary, a breakdown by category, the total spent, and three ways to save money.

8. Saved sessions
Every session is saved in a file. The user can open it later from the menu and read the conversation again.