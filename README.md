# Auto Resume Sender 
Executive résumé generator that produces a premium PDF and optionally emails it to the recipient in 1 click. The React front end collects rich candidate data; the Flask backend orchestrates LLM text generation, PDF rendering, SQLite storage, and SMTP delivery.

## Prerequisites
- Python 3.9+
- Node.js 18+
- (Optional) SMTP account (Gmail, SendGrid, etc.)
- (Optional) OpenAI API key if you want AI-authored résumés

---

## 1. Backend setup
```bash
cd backend
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```

### Environment configuration (`backend/.env`)
- `EMAIL_PROVIDER`: `SMTP` to send mail, `NONE` to disable (safe default for dev).
- `SMTP_HOST`, `SMTP_PORT`, `SMTP_USER`, `SMTP_PASS`, `SENDER_EMAIL`, `SENDER_NAME`: fill when email is enabled. Gmail requires 2FA + App Password; use the Gmail address for both `SMTP_USER` and `SENDER_EMAIL`.
- `LLM_PROVIDER`: set to `OPENAI` and supply `OPENAI_API_KEY` to use GPT-generated content; leave as `NONE` for the built-in template.
- `PDF_PROVIDER`: defaults to `REPORTLAB`; leave unless you intentionally disable PDFs.

`.env` is ignored by Git—keep secrets there or inject them via your deploy platform.

### Optional providers
```bash
pip install reportlab   # PDF writer (already required for default setup)
pip install openai      # Only if LLM_PROVIDER=OPENAI
```

### Useful backend commands
```bash
python -m backend.app    # run API at http://localhost:5001
pytest -q                # backend tests
python -m backend.scripts.worker  # process queued submissions (not needed when we auto-send)
```

Generated assets are stored under `data/`:
- `data/app.db` — SQLite submissions log
- `data/resumes/*.pdf` — résumé output files

---

## 2. Frontend setup
```bash
cd frontend
npm install
npm run dev        # http://localhost:5173 (executive dark UI)
npm run test       # Vitest
npm run typecheck  # TypeScript compiler in noEmit mode
```

Submitting the form POSTs to `/api/submit`, generates the PDF, records the submission, and—when SMTP credentials are present—sends the email immediately.

---

## 3. Deployment checklist
- Provide production SMTP credentials via environment variables.
- Set `LLM_PROVIDER=OPENAI` and `OPENAI_API_KEY` if you want AI-authored résumés in prod.
- Mount persistent storage for `data/` if you need to retain PDFs and submission history.
- Schedule the worker (`python -m backend.scripts.worker`) only if you later switch back to queued delivery.
- Keep personal onboarding notes in `docs/` (ignored by Git) or convert them into formal documentation before pushing.
