# (STEP 2 • Data) Centralize config; add dirs
import os
from dataclasses import dataclass

# Load environment from .env if python-dotenv is available
try:
    from dotenv import load_dotenv  # type: ignore
    # Try project root and backend directory
    _CWD = os.path.abspath(os.path.dirname(__file__))
    load_dotenv(os.path.abspath(os.path.join(_CWD, "..", ".env")), override=False)
    load_dotenv(os.path.join(_CWD, ".env"), override=False)
except Exception:
    pass

# Resolve paths relative to project base (../ from this file)
_BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

def _resolve_path(p: str) -> str:
    """Return absolute path; resolve relative to project base when not absolute."""
    return p if os.path.isabs(p) else os.path.abspath(os.path.join(_BASE_DIR, p))

@dataclass
class Settings:
    SECRET_KEY: str = os.getenv("SECRET_KEY", "dev")
    PORT: int = int(os.getenv("PORT", "5001"))

    # Make data/log dirs absolute to avoid sandbox issues
    DATA_DIR: str = _resolve_path(os.getenv("DATA_DIR", "data"))
    LOG_DIR: str = _resolve_path(os.getenv("LOG_DIR", "logs"))

    EMAIL_PROVIDER: str = os.getenv("EMAIL_PROVIDER", "SMTP").upper()   # SMTP | NONE
    PDF_PROVIDER: str = os.getenv("PDF_PROVIDER", "REPORTLAB").upper()  # REPORTLAB | NONE
    LLM_PROVIDER: str = os.getenv("LLM_PROVIDER", "NONE").upper()       # OPENAI | NONE

    SMTP_HOST: str = os.getenv("SMTP_HOST", "smtp.gmail.com")
    SMTP_PORT: int = int(os.getenv("SMTP_PORT", "587"))
    SMTP_USER: str = os.getenv("SMTP_USER", "")
    SMTP_PASS: str = os.getenv("SMTP_PASS", "")
    SENDER_NAME: str = os.getenv("SENDER_NAME", "Auto Sender Bot")
    SENDER_EMAIL: str = os.getenv("SENDER_EMAIL", "example@example.com")

    OPENAI_API_KEY: str = os.getenv("OPENAI_API_KEY", "")

settings = Settings()
