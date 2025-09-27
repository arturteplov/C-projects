"""
(STEP 5 • Adapters) Choose providers from env

Make optional providers lazy-imported so missing third‑party packages
do not crash app startup. Fall back gracefully when unavailable.
"""
from ..settings import settings

class Adapters:
    def __init__(self):
        self.llm = self._llm()
        self.pdf = self._pdf()
        self.email = self._email()

    def _llm(self):
        # Always have a fallback LLM
        try:
            from .llm.none_llm import NoneLlmAdapter
        except Exception:
            NoneLlmAdapter = None  # type: ignore

        if settings.LLM_PROVIDER == "OPENAI" and settings.OPENAI_API_KEY:
            try:
                from .llm.openai_llm import OpenAiLlmAdapter
                return OpenAiLlmAdapter()
            except Exception:
                # fall back if openai client not installed/usable
                pass
        # default / fallback
        return NoneLlmAdapter() if NoneLlmAdapter else None

    def _pdf(self):
        if settings.PDF_PROVIDER == "REPORTLAB":
            try:
                from .pdf.reportlab_pdf import ReportLabPdfAdapter
                return ReportLabPdfAdapter()
            except Exception:
                # reportlab not installed or import error
                return None
        return None  # none

    def _email(self):
        if settings.EMAIL_PROVIDER == "SMTP":
            try:
                from .email.smtp_email import SmtpEmailAdapter
                return SmtpEmailAdapter()
            except Exception:
                return None
        return None  # none

adapters = Adapters()
