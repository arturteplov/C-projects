# (STEP 3 • Core logic) Orchestrate: text -> PDF -> DB -> optional send
import os
import re
from ..db import get_conn
from ..settings import settings
from ..adapters.registry import adapters


def _slugify(value: str) -> str:
    clean = re.sub(r"[^A-Za-z0-9]+", "_", value.strip())
    return clean.strip("_") or "candidate"


class SubmissionService:
    def create(
        self,
        *,
        full_name: str,
        target_role: str,
        to_email: str,
        experience: str,
        send_now: bool,
        summary: str = "",
        skills: str = "",
        education: str = "",
        projects: str = "",
        contact_email: str = "",
        phone: str = "",
        location: str = "",
        portfolio: str = "",
        linkedin: str = "",
    ):
        text = adapters.llm.resume_text(
            full_name,
            target_role,
            experience,
            summary,
            skills,
            education,
            projects,
            contact_email,
            phone,
            location,
            portfolio,
            linkedin,
        )

        # write PDF (or text file if no PDF adapter)
        pdf_rel = (
            "resumes/"
            f"{_slugify(full_name)}_"
            f"{_slugify(to_email.replace('@', '_at_'))}.pdf"
        )
        pdf_path = os.path.join(settings.DATA_DIR, pdf_rel)
        if adapters.pdf:
            adapters.pdf.write_pdf(text, pdf_path)
        else:
            os.makedirs(os.path.dirname(pdf_path), exist_ok=True)
            with open(pdf_path, "w") as f:
                f.write(text)

        # DB row
        with get_conn() as c:
            cur = c.cursor()
            cur.execute(
                """
                INSERT INTO submissions (
                    full_name, target_role, to_email, experience, pdf_path, status,
                    contact_email, phone, location, summary, skills, education, projects, portfolio, linkedin
                ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
                """,
                (
                    full_name,
                    target_role,
                    to_email,
                    experience,
                    pdf_rel,
                    "generated" if send_now else "queued",
                    contact_email,
                    phone,
                    location,
                    summary,
                    skills,
                    education,
                    projects,
                    portfolio,
                    linkedin,
                ),
            )
            sub_id = cur.lastrowid

        # optional send now
        if send_now and adapters.email:
            subject = f"{full_name} — Application for {target_role or 'the role'}"
            body_lines = [
                "Hello,",
                "",
                "Please find attached my resume.",
                "",
                "Candidate contact:",
            ]
            if contact_email:
                body_lines.append(f"Email: {contact_email}")
            if phone:
                body_lines.append(f"Phone: {phone}")
            if location:
                body_lines.append(f"Location: {location}")
            if portfolio:
                body_lines.append(f"Portfolio: {portfolio}")
            if linkedin:
                body_lines.append(f"LinkedIn: {linkedin}")
            body_lines.extend(["", "Best,", full_name])
            body = "\n".join(body_lines)
            try:
                adapters.email.send(to_email, subject, body, pdf_path)
                with get_conn() as c:
                    c.execute("UPDATE submissions SET status='sent', sent_at=CURRENT_TIMESTAMP WHERE id=?", (sub_id,))
            except Exception as e:
                # Record failure but do not crash the request
                with get_conn() as c:
                    c.execute("UPDATE submissions SET status='failed', error=? WHERE id=?", (str(e), sub_id))

        return sub_id, pdf_rel

service = SubmissionService()
