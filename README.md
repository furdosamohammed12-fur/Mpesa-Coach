# Pesa Coach

A command-line money coach for young Kenyans. The user types what they spent. The coach sorts each expense into a category, keeps running totals in Kenyan shillings (KES), answers questions about spending, and writes an end-of-session summary with three ways to save.

**Author:** Furdosa Mohammed
**Course:** WeCan Academy, AI Season 12
**Date:** 27 November 2026

---

## What it does

- Sorts expenses into transport, food, airtime, rent, shopping, or other
- Keeps running totals for each category
- Remembers the whole conversation, so the user can ask follow-up questions
- Adds real saving tips from a built-in knowledge base (RAG)
- Checks every AI reply and retries once if the format is wrong
- Answers from saved totals when the AI cannot be reached (offline mode)
- Writes a summary at the end and saves every session to a file

## How it works

1. **Menu.** The user starts a new session, opens a past session, or exits.
2. **Prompts (RTCCO).** The AI is given a Role, Task, Context, Constraints and Output format. A second prompt of the same kind is used for the summary.
3. **AI model.** Messages go to Google Gemini. It replies in JSON with `reply`, `total_spent` and `totals`.
4. **Reply check.** `check_reply()` confirms the JSON is complete. If not, the program asks once more.
5. **Knowledge base (RAG).** `find_tips()` matches keywords in the message (for example "matatu" or "airtime") and gives the matching tips to Gemini.
6. **Memory.** The full conversation is sent with every request.
7. **Cache and offline mode.** After each good reply, the latest totals are saved to `cache.json`. If the AI is unreachable, `offline_reply()` answers from that file.
8. **Summary.** When the user types `exit`, Gemini writes a summary, a breakdown by category, the total spent, and three ways to save.
9. **Saved sessions.** Each session is saved as `sessions/session_<date>_<time>.json` and can be opened from the menu.

## Files

| File | Purpose |
|------|---------|
| `mpesa.py` | The whole program |
| `.env` | Holds the API key (never upload this) |
| `cache.json` | Latest saved totals, used offline |
| `sessions/` | Saved conversations and summaries |
| `requirements.txt` | Libraries to install |

## Requirements

- Python 3.10 or newer
- A Google Gemini API key
- Libraries: `google-genai`, `python-dotenv`

## Setup

1. Open the project folder in VS Code.
2. Create and activate a virtual environment:
   ```
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install the libraries:
   ```
   pip install -r requirements.txt
   ```
4. Create a file named `.env` in the project folder with this line:
   ```
   API_KEY=your_key_here
   ```

## How to run

```
python mpesa.py
```

Choose option 1, then type an expense, for example `I spent 200 on matatu`. Type `exit` to end the session and see the summary.

## Testing checklist

Run each test and save a screenshot in a `samples/` folder.

- [ ] Add an expense with an amount (for example "I spent 200 on matatu")
- [ ] Add two expenses in one message
- [ ] Send an expense with no amount (the coach should ask for it)
- [ ] Press Enter with nothing typed (should ask the user to type something)
- [ ] Ask "How much have I spent on food?" (tests memory)
- [ ] Mention "airtime" or "matatu" (tests the knowledge base tip)
- [ ] Turn off the internet and ask for totals (tests offline mode)
- [ ] Type `exit` and read the summary
- [ ] Open the saved session from menu option 2

## Example session

```
You: I spent 200 on matatu and 150 on lunch
Coach: [paste the real reply]
You: exit
--- Session summary ---
[paste the real summary]
```

## Limitations

- Offline mode can only report saved totals. It cannot record new expenses.
- The coach knows only what the user types. It does not read M-Pesa messages.
- The knowledge base is small and matches keywords only.
- It runs in the terminal and has no web interface.

## Safety

- The API key is kept in `.env`, which must be listed in `.gitignore` and never uploaded to GitHub.
- The coach is told to use only amounts the user gave and to ask when an amount is missing.
