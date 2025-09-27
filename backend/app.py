#1.1 Creating API  /api/ping + /api/submit

#Risks & debug: Bad JSON parsing, CORS, 400/500 errors.
#Monitor: Add request logs; use curl/Postman; log 4xx/5xx with payload size + req ID.
#Quick checks: curl localhost:5001/api/ping should return {"ok": true}.


import os, logging
from flask import Flask, request, jsonify
from .settings import settings
from .db import init_db
from .services.submissions import service

os.makedirs(settings.LOG_DIR, exist_ok=True)
logging.basicConfig(level=logging.INFO)

app = Flask(__name__)
app.config["SECRET_KEY"] = settings.SECRET_KEY

init_db()

@app.get("/api/ping")
def ping():
    return {"ok": True, "msg": "online"}

@app.post("/api/submit")
def submit():
    d = request.get_json(force=True)
    for k in ["fullName", "toEmail"]:
        if not d.get(k):
            return jsonify({"ok": False, "error": f"Missing {k}"}), 400
    sid, pdf_rel = service.create(
        full_name=d["fullName"].strip(),
        target_role=(d.get("targetRole") or "").strip(),
        to_email=d["toEmail"].strip(),
        experience=(d.get("experience") or "").strip(),
        summary=(d.get("summary") or "").strip(),
        skills=(d.get("skills") or "").strip(),
        education=(d.get("education") or "").strip(),
        projects=(d.get("projects") or "").strip(),
        contact_email=(d.get("candidateEmail") or "").strip(),
        phone=(d.get("phone") or "").strip(),
        location=(d.get("location") or "").strip(),
        portfolio=(d.get("portfolio") or "").strip(),
        linkedin=(d.get("linkedin") or "").strip(),
        send_now=bool(d.get("sendNow")),
    )
    return {"ok": True, "id": sid, "pdf": pdf_rel}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=settings.PORT, debug=True)
