# ==========================================================
# DEEP EMOTIONS — CONFIGURATION
# ==========================================================

import os

from dotenv import load_dotenv


# ==========================================================
# LOAD ENVIRONMENT VARIABLES
# ==========================================================

load_dotenv()


# ==========================================================
# TELEGRAM BOT
# ==========================================================

BOT_TOKEN = os.getenv(
    "BOT_TOKEN",
    "",
).strip()


# ==========================================================
# GEMINI AI
# ==========================================================

GEMINI_API_KEY = os.getenv(
    "GEMINI_API_KEY",
    "",
).strip()

GEMINI_MODEL = os.getenv(
    "GEMINI_MODEL",
    "gemini-3.8-flash",
).strip()


# ==========================================================
# OWNER
# ==========================================================

try:

    OWNER_ID = int(
        os.getenv(
            "OWNER_ID",
            "0",
        )
        or 0
    )

except ValueError:

    OWNER_ID = 0


# ==========================================================
# VALIDATION
# ==========================================================

if not BOT_TOKEN:

    raise RuntimeError(
        "BOT_TOKEN missing. "
        "Set BOT_TOKEN in your local .env or in Heroku Config Vars."
    )


if not GEMINI_API_KEY:

    raise RuntimeError(
        "GEMINI_API_KEY missing. "
        "Set GEMINI_API_KEY in your local .env or in Heroku Config Vars."
    )


# ==========================================================
# CONFIG SUMMARY
# ==========================================================

print(
    f"Deep Emotions config loaded | "
    f"Model: {GEMINI_MODEL}"
)
