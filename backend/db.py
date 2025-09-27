# (STEP 2 • Data) SQLite + submissions table
import os, sqlite3
from .settings import settings

DB_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "app.db")

SCHEMA = """
CREATE TABLE IF NOT EXISTS submissions (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  full_name TEXT NOT NULL,
  target_role TEXT,
  to_email TEXT NOT NULL,
  experience TEXT,
  pdf_path TEXT,
  status TEXT DEFAULT 'queued',
  error TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
  sent_at DATETIME,
  contact_email TEXT,
  phone TEXT,
  location TEXT,
  summary TEXT,
  skills TEXT,
  education TEXT,
  projects TEXT,
  portfolio TEXT,
  linkedin TEXT
);
"""

EXTRA_COLUMNS = {
    "contact_email": "TEXT",
    "phone": "TEXT",
    "location": "TEXT",
    "summary": "TEXT",
    "skills": "TEXT",
    "education": "TEXT",
    "projects": "TEXT",
    "portfolio": "TEXT",
    "linkedin": "TEXT",
}

def get_conn():
    os.makedirs(os.path.join(os.path.dirname(__file__), "..", "data"), exist_ok=True)
    conn = sqlite3.connect(DB_PATH, check_same_thread=False)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_conn() as c:
        c.executescript(SCHEMA)
        for col, col_type in EXTRA_COLUMNS.items():
            try:
                c.execute(f"ALTER TABLE submissions ADD COLUMN {col} {col_type}")
            except sqlite3.OperationalError:
                pass
