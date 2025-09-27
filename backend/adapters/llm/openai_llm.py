# (STEP 5 • Adapters) Optional OpenAI LLM
from .base import LlmAdapter
from ...settings import settings


class OpenAiLlmAdapter(LlmAdapter):
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
        try:
            from openai import OpenAI

            client = OpenAI(api_key=settings.OPENAI_API_KEY)
            prompt = (
                "You are a world-class resume writer crafting content for an executive. "
                "Use the data provided to produce a polished resume in plain text with sections: "
                "DETAILS, SUMMARY, SKILLS, EXPERIENCE, PROJECTS, EDUCATION. "
                "Bullet appropriate sections with '- '. Keep tone confident and concise.\n\n"
                f"Name: {full_name}\n"
                f"Target Role: {role or 'Open to opportunities'}\n"
                f"Contact Email: {contact_email}\n"
                f"Phone: {phone}\n"
                f"Location: {location}\n"
                f"Portfolio: {portfolio}\n"
                f"LinkedIn: {linkedin}\n"
                f"Summary hints: {summary}\n"
                f"Top skills: {skills}\n"
                f"Experience bullets: {experience}\n"
                f"Projects: {projects}\n"
                f"Education details: {education}\n"
                "Return only the resume text in that order."
            )
            r = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You create exceptional executive resumes."},
                    {"role": "user", "content": prompt},
                ],
                temperature=0.35,
            )
            return r.choices[0].message.content.strip()
        except Exception as e:
            return f"AI unavailable ({e}); using fallback text."
