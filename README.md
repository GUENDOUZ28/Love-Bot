# 💕 Fatima & Hakim's Love & Games Telegram Bot 🎮

A private, romantic Telegram companion bot created specifically for **Fatima** by **Hakim**. 

Unlike generic quote bots, this bot is designed as an intimate relationship sanctuary — packed with tender love messages, interactive date night planners, fun couple games, a virtual love letter generator, and a private Love Jar for secret notes.

---

## ✨ Features Overview

### 💌 1. Heartfelt Love Messages & Whispers
- **Why I Love You (90+ Reasons):** Heart-melting reasons why Hakim adores Fatima (e.g. *“The way you scrunch your nose when you're being playful”*, *“How safe my heart feels with you”*).
- **Good Morning Whispers:** Gentle, sunshine-filled morning messages customized with her nickname to start her day with a smile.
- **Good Night Whispers:** Cozy, tender messages with virtual tuck-ins and forehead kisses.
- **Sweet Compliments:** Random heartfelt reminders of her beauty, grace, and intelligence.
- **Interactive Hugs & Kisses Counter:** Send virtual hugs (`🫂`) and kisses (`💋`) with an ongoing couple counter (`"Hakim has delivered 42 hugs and 100 kisses!"`).

### 📜 2. Romantic Love Letter Generator
Tailor-made love letters signed by Hakim for any mood:
- 💖 *Just Because I Love You*
- 🥺 *When I Miss You*
- 🌸 *Comfort & Reassurance (For tough or tiring days)*
- 💍 *Our Anniversary & Milestones*
- 🏡 *Dreaming of Our Future Together*

### 🎡 3. Date Night Planner & Wishlist
- **🎲 Spin the Date Wheel:** Generates surprise date ideas across categories (*Cozy At-Home*, *Foodie & Romantic*, *Outdoor Adventures*).
- **📌 Save to Our Bucket List:** Save favorite ideas directly into the couple wishlist.
- **📋 Wishlist Viewer:** View all planned adventures anytime.

### 🎮 4. Couple Games & Fun
- **🥠 Daily Love Fortune Cookie:** Fatima can crack open a daily fortune cookie with a sweet prediction from Hakim.
- **❓ Couple Quiz:** *"How Well Do You Know Hakim & Fatima?"* — interactive quiz with instant feedback and score tracking.
- **⚖️ Couples "Would You Rather?":** Cute, funny, and romantic dilemmas designed for couples.
- **🎯 Truth or Dare (Romantic Edition):** Sweet truth prompts and playful dares (voice notes, selfies, long hugs).

### 🫙 5. The Virtual Love Jar
- **✍️ Drop a Secret Note:** Hakim or Fatima can type a message in chat to fold and seal inside the jar.
- **🫙 Draw a Secret Note:** Fatima can open a note whenever she misses Hakim or needs encouragement.

### ⏳ 6. Our Love Story Counter
- Calculates exact **days, hours, and time together** since your anniversary.
- Displays couple milestone stats.

---

## 🚀 Quick Setup Guide (2 Minutes)

### 1. Prerequisites
- Python 3.10+ installed (Python 3.14 is tested and verified).

### 2. Create Your Bot on Telegram
1. Open Telegram and search for **[@BotFather](https://t.me/BotFather)**.
2. Send `/newbot` to BotFather.
3. Choose a sweet name (e.g., `Fatima & Hakim 💕` or `Our Love Sanctuary`).
4. Choose a username ending in `bot` (e.g., `FatimaHakimLoveBot`).
5. BotFather will provide an **HTTP API Token** (e.g., `7123456789:AAH...`).

### 3. Configure the Bot
Copy the `.env.example` file to `.env`:
```powershell
Copy-Item .env.example .env
```
Open `.env` and fill in your details:
```env
TELEGRAM_BOT_TOKEN=your_token_from_botfather_here

# (Optional) Anniversary date (YYYY-MM-DD)
ANNIVERSARY_DATE=2024-01-01

# Names & Nicknames
BOYFRIEND_NAME=Hakim
GIRLFRIEND_NAME=Fatima
FATIMA_NICKNAMES=Fatima,Fatimati,Hayati,Mon amour,Habibati,Princesse,My Queen,Amouna
```

### 4. Install Dependencies
Dependencies are already installed, or run:
```powershell
py -m pip install -r requirements.txt
```

### 5. Start the Bot
Run:
```powershell
py bot.py
```

---

## 📱 How to Use on Telegram

1. Open your bot on Telegram and send `/start`.
2. To find your exact Telegram User ID (and Fatima's), send `/id`. You can paste these into `HAKIM_USER_ID` and `FATIMA_USER_ID` in `.env` so the bot automatically recognizes each of you when you speak to it!
3. Tap on any button in the interactive keyboard menu to explore messages, letters, games, and dates.

---

## 🗂️ Project Structure

```
Love bot/
├── bot.py                  # Main Telegram bot application & router
├── config.py               # Environment configuration & couple settings
├── database.py             # SQLite database for notes jar, wishlist, counters
├── test_bot.py             # Automated test suite
├── requirements.txt        # Python libraries
├── .env.example            # Environment variables template
├── .env                    # Real credentials (keep private)
├── data/
│   ├── love_reasons.py     # 90+ romantic reasons why Hakim loves Fatima
│   ├── love_messages.py    # Morning, Night, Compliments, Hugs & Kisses
│   ├── love_letters.py     # Multi-occasion romantic love letter generator
│   ├── date_ideas.py       # Categorized date night suggestions & tips
│   └── couple_games.py     # Quizzes, Would You Rather, Truth or Dare, Fortunes
└── handlers/
    ├── start.py            # Welcome greeting & main menu keyboard
    ├── love_messages.py    # Love messages, hugs, kisses & reasons handlers
    ├── love_letters.py     # Interactive letter generator handler
    ├── dates.py            # Date ideas, spinner & wishlist handlers
    ├── games.py            # Couple games & quiz handlers
    ├── love_jar.py         # Secret love notes jar handlers
    └── love_counter.py     # Days together & stats counter
```

---

## 🔒 Privacy & Exclusivity
- The bot stores your custom notes and counters locally in a lightweight SQLite database (`love_bot.db`).
- Setting `HAKIM_USER_ID` and `FATIMA_USER_ID` in `.env` personalizes the experience specifically for Fatima and Hakim.
