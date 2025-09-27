# (STEP 5 • Adapters) Fallback LLM that returns templated text
from .base import LlmAdapter


def _split_items(text: str) -> list[str]:
    items = []
    if text:
        for line in text.replace("\r", "").splitlines():
            normalized = line.strip(" \t•-")
            if normalized:
                items.append(normalized)
        if not items and "," in text:
            items = [p.strip() for p in text.split(",") if p.strip()]
    return items


def _bulletize(items: list[str]) -> list[str]:
    return [f"- {item}" for item in items] if items else ["- —"]


class NoneLlmAdapter(LlmAdapter):
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
        clean_name = full_name.strip() or "Candidate Name"
        role_line = role.strip() or "Open to opportunities"
        contact_line = " | ".join(
            [
                part
                for part in [
                    contact_email.strip() or "email unavailable",
                    phone.strip() or "phone unavailable",
                    location.strip() or "location flexible",
                ]
                if part
            ]
        )

        details = []
        if contact_email.strip():
            details.append(f"Email: {contact_email.strip()}")
        if phone.strip():
            details.append(f"Phone: {phone.strip()}")
        if location.strip():
            details.append(f"Location: {location.strip()}")
        if portfolio.strip():
            details.append(f"Portfolio: {portfolio.strip()}")
        if linkedin.strip():
            details.append(f"LinkedIn: {linkedin.strip()}")
        if not details:
            details.append("Email: email unavailable")
        skills_items = _split_items(skills)
        experience_items = _split_items(experience) or ["Drive initiatives end-to-end and deliver measurable impact."]
        project_items = _split_items(projects)
        education_items = _split_items(education) or ["Self-guided learning and continuous upskilling"]

        summary_text = (summary.strip() or f"Strategic leader ready to excel in {role_line}.")

        lines = [
            clean_name,
            f"Target Role: {role_line}",
            f"Contact: {contact_line}",
            "",
            "DETAILS",
            *details,
            "",
            "SUMMARY",
            summary_text,
            "",
            "SKILLS",
            *_bulletize(skills_items or ["Cross-functional collaboration", "Product strategy", "Delivery excellence"]),
            "",
            "EXPERIENCE",
            *_bulletize(experience_items),
            "",
            "PROJECTS",
            *(_bulletize(project_items) if project_items else ["- Delivered automation that saved 200+ hours per quarter."]),
            "",
            "EDUCATION",
            *_bulletize(education_items),
        ]

        return "\n".join(lines).strip() + "\n"
