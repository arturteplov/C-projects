# (STEP 5 • Adapters) LLM interface
from abc import ABC, abstractmethod


class LlmAdapter(ABC):
    @abstractmethod
    def resume_text(
        self,
        full_name: str,
        role: str,
        experience: str,
        summary: str,
        skills: str,
        education: str,
        projects: str,
        contact_email: str,
        phone: str,
        location: str,
        portfolio: str,
        linkedin: str,
    ) -> str:
        """Return plain-text resume content for downstream PDF rendering."""
