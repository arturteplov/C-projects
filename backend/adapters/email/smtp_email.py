# (STEP 5 • Adapters) SMTP email sender (use Gmail App Password for dev)
import os, smtplib, mimetypes
from email.message import EmailMessage
from ...settings import settings
from .base import EmailAdapter
from typing import Optional
import base64

class SmtpEmailAdapter(EmailAdapter):
    def send(self, to_email: str, subject: str, body: str, attachment_path: Optional[str]  = None) -> None:
        msg = EmailMessage()
        msg["From"] = f"{settings.SENDER_NAME} <{settings.SENDER_EMAIL}>"
        msg["To"] = to_email
        msg["Subject"] = subject
        msg.set_content(body)
        if attachment_path:
            ctype, _ = mimetypes.guess_type(attachment_path)
            maintype, subtype = (ctype or "application/octet-stream").split("/", 1)
            with open(attachment_path, "rb") as f:
                msg.add_attachment(f.read(), maintype=maintype, subtype=subtype, filename=os.path.basename(attachment_path))
        with smtplib.SMTP(settings.SMTP_HOST, settings.SMTP_PORT) as server:
            # Be explicit with EHLO and TLS for better compatibility
            server.ehlo()
            server.starttls()
            server.ehlo()

            # Some Python 3.9 builds have a bytes/str bug in smtplib.login.
            # Try normal login first, then fall back to manual AUTH LOGIN.
            try:
                server.login(str(settings.SMTP_USER or ''), str(settings.SMTP_PASS or ''))
            except TypeError:
                # Manual AUTH LOGIN dance using only strings
                code, _ = server.docmd("AUTH", "LOGIN")
                if code != 334:
                    raise smtplib.SMTPException("AUTH LOGIN not accepted")
                # Username prompt
                code, _ = server.docmd(base64.b64encode((settings.SMTP_USER or '').encode()).decode())
                if code != 334:
                    raise smtplib.SMTPAuthenticationError(code, "Username not accepted")
                # Password prompt
                code, _ = server.docmd(base64.b64encode((settings.SMTP_PASS or '').encode()).decode())
                if code != 235:
                    raise smtplib.SMTPAuthenticationError(code, "Authentication failed")

            server.send_message(msg)
