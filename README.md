# 𝐃ᴇᴇᴘ 𝐄ᴍᴏᴛɪᴏɴs

Telegram + Gemini AI chatbot with long-term memory,
group conversation context, AI tools, voice support,
privacy controls and basic moderation.

## ✨ Features

- 🤖 Gemini AI conversations
- 🧠 Long-term personal memory
- 💬 Group conversation context
- 👋 Welcome and goodbye messages
- 🛡️ Basic anti-spam moderation
- 🛠️ AI tools
  - Rewrite
  - Summarize
  - Translate
  - Explain
  - Study Help
- 🎙️ Voice message transcription
- 🔒 Privacy and memory controls
- 📊 User statistics
- ⚡ Rate limiting
- 🌐 Render health server support

## 📁 Project Structure

```text
TelegramAIBot/
├── .env
├── .env.example
├── .gitignore
├── config.py
├── main.py
├── requirements.txt
├── README.md
├── data/
│   └── deep_emotions.db
├── bot/
│   ├── __init__.py
│   ├── ai.py
│   ├── database.py
│   └── handlers.py
└── .venv/

## 🚀 Deploy on Heroku

This project includes a `Procfile`, `runtime.txt`, and `app.json` for Heroku.

1. Upload this project to a **private GitHub repository** (do not upload `.env` or real API keys).
2. In Heroku, create an app and connect the GitHub repository under **Deploy**.
3. In **Settings → Config Vars**, add:
   - `BOT_TOKEN` — token from Telegram's official @BotFather.
   - `GEMINI_API_KEY` — a newly generated key from Google AI Studio.
   - `GEMINI_MODEL` — `gemini-2.5-flash` (optional; this is the default).
   - `OWNER_ID` — your numeric Telegram user ID (optional; set `0` only if you do not use owner-only features).
4. Deploy the branch, then open **More → View logs** to check startup.
5. Keep one web dyno running. The web process also serves a health-check endpoint on Heroku's `PORT`.

### Security
- Never put bot tokens or API keys in source code, ZIP files, screenshots, or public repositories.
- A Gemini key shared in a chat should be considered exposed: revoke it and create a replacement in Google AI Studio, then save the replacement only in Heroku Config Vars.
- If the bot token was exposed, revoke/regenerate it with @BotFather too.
- Heroku may require a paid dyno; check the current plan and pricing in your Heroku dashboard.
