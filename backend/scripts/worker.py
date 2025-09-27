# (STEP 6 • Background) Process queued submissions in batches (run via cron)
import os, sqlite3
from backend.db import DB_PATH
from backend.settings import settings
from backend.adapters.registry import adapters

DATA_DIR = settings.DATA_DIR

with sqlite3.connect(DB_PATH) as conn:
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("SELECT * FROM submissions WHERE status='queued' ORDER BY created_at ASC LIMIT 10")
    rows = cur.fetchall()
    for r in rows:
        pdf_path = os.path.join(DATA_DIR, r["pdf_path"])
        subject = f"{r['full_name']} — Application for {r['target_role'] or 'the role'}"
        body_lines = [
            "Hello,",
            "",
            "Please find attached my resume.",
            "",
            "Candidate contact:",
        ]
        if r["contact_email"]:
            body_lines.append(f"Email: {r['contact_email']}")
        if r["phone"]:
            body_lines.append(f"Phone: {r['phone']}")
        if r["location"]:
            body_lines.append(f"Location: {r['location']}")
        if r["portfolio"]:
            body_lines.append(f"Portfolio: {r['portfolio']}")
        if r["linkedin"]:
            body_lines.append(f"LinkedIn: {r['linkedin']}")
        body_lines.extend(["", "Best,", r['full_name']])
        body = "\n".join(body_lines)
        if adapters.email:
            try:
                adapters.email.send(r["to_email"], subject, body, pdf_path)
                cur.execute("UPDATE submissions SET status='sent', sent_at=CURRENT_TIMESTAMP WHERE id=?", (r["id"],))
                conn.commit()
                print("sent", r["id"])
            except Exception as e:
                cur.execute("UPDATE submissions SET status='failed', error=? WHERE id=?", (str(e), r["id"]))
                conn.commit()
                print("fail", r["id"], e)
