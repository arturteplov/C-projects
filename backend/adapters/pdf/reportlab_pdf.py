# (STEP 5 • Adapters) Simple PDF writer with ReportLab
import os
import unicodedata
from typing import Dict, List, Tuple
from reportlab.lib.pagesizes import LETTER
from reportlab.lib import colors
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from .base import PdfAdapter


def _sanitize_ascii(s: str) -> str:
    # Replace common unicode punctuation with ASCII-friendly equivalents
    s = (
        s.replace("•", "- ")
         .replace("–", "-")
         .replace("—", "-")
         .replace("’", "'")
         .replace("“", '"')
         .replace("”", '"')
    )
    # Strip unsupported glyphs for built-in Type1 fonts
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode("ascii")
    return s


def _wrap_draw(c: canvas.Canvas, text: str, x: float, y: float, max_w: float, line_h: float, font_name: str, font_size: float, bottom_margin: float) -> float:
    """Draw wrapped text and return updated y."""
    for raw_line in (text.splitlines() or [text]):
        line = _sanitize_ascii(raw_line)
        if line.strip() == "":
            y -= line_h
            if y < bottom_margin:
                c.showPage(); c.setFont(font_name, font_size); y = LETTER[1] - bottom_margin
            continue
        words = line.split()
        cur = ""
        for w in words:
            test = (cur + " " + w).strip()
            if pdfmetrics.stringWidth(test, font_name, font_size) <= max_w:
                cur = test
            else:
                if y < bottom_margin:
                    c.showPage(); c.setFont(font_name, font_size); y = LETTER[1] - bottom_margin
                c.drawString(x, y, cur)
                y -= line_h
                cur = w
        if cur:
            if y < bottom_margin:
                c.showPage(); c.setFont(font_name, font_size); y = LETTER[1] - bottom_margin
            c.drawString(x, y, cur)
            y -= line_h
    return y


SECTION_ORDER = [
    "DETAILS",
    "SUMMARY",
    "SKILLS",
    "EXPERIENCE",
    "PROJECTS",
    "EDUCATION",
    "LANGUAGES",
    "CERTIFICATIONS",
]

TITLE_ALIASES = {
    "SUMMARY": "PROFILE",
}


def _parse_sections(text: str) -> Tuple[str, str, Dict[str, List[str]]]:
    """Parse simple resume text into sections. Returns (name, role, sections)."""
    content = (text or "").splitlines()
    name = _sanitize_ascii(content[0].strip()) if content else ""
    role = ""
    idx = 1
    if idx < len(content) and content[idx].startswith("Target Role:"):
        role = _sanitize_ascii(content[idx].split(":", 1)[1].strip())
        idx += 1
    # Skip blanks
    while idx < len(content) and content[idx].strip() == "":
        idx += 1

    sections: Dict[str, List[str]] = {key: [] for key in SECTION_ORDER}

    # Capture contact lines before first explicit section (e.g. "Contact: ...")
    while idx < len(content) and content[idx].strip() and content[idx].strip().upper() not in sections:
        sections["DETAILS"].append(content[idx])
        idx += 1

    current = None
    known = set(sections.keys())
    for line in content[idx:]:
        s = line.strip()
        if not s:
            continue
        if s.upper() in known:
            current = s.upper()
            continue
        if current is None:
            # If no explicit summary header, treat leading lines as summary
            current = "SUMMARY"
        sections[current].append(line)
    return name, role, sections


class ReportLabPdfAdapter(PdfAdapter):
    def write_pdf(self, text: str, out_path: str) -> None:
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        c = canvas.Canvas(out_path, pagesize=LETTER)

        page_w, page_h = LETTER
        margin = 50
        max_w = page_w - margin * 2
        x = margin
        y = page_h - margin
        bottom = margin
        line_h = 15

        # Fonts
        base_font = "Helvetica"
        bold_font = "Helvetica-Bold"
        small_font = "Helvetica"

        name, role, sections = _parse_sections(text or "")

        # Pure black header: large name and role, no background color
        c.setFillColor(colors.black)
        title = name or "Resume"
        c.setFont(bold_font, 24)
        c.drawString(x, y, _sanitize_ascii(title))
        y -= line_h
        if role:
            c.setFont(base_font, 12)
            c.drawString(x, y, _sanitize_ascii(role))
            y -= line_h
        y -= 8

        # Two-column layout: left (details/skills), right (profile/experience/education)
        gutter = 24
        left_w = max(180, int(max_w * 0.32))
        right_w = max_w - left_w - gutter
        left_x = x
        right_x = x + left_w + gutter

        # Vertical divider (subtle gray)
        c.setStrokeColor(colors.Color(0.75, 0.75, 0.75))
        c.setLineWidth(0.5)
        c.line(right_x - gutter/2, bottom, right_x - gutter/2, page_h - margin)
        c.setStrokeColor(colors.black)

        # Section renderer
        def section(title: str, body_lines: List[str]):
            nonlocal y
            if y - (line_h * 3) < bottom:
                c.showPage(); y = page_h - margin
            # Title with thin gray rule
            display_title = TITLE_ALIASES.get(title.upper(), title.upper())
            c.setFont(bold_font, 12)
            c.setFillColor(colors.black)
            c.drawString(cur_x, y, display_title)
            y -= line_h - 6
            c.setStrokeColor(colors.Color(0.85, 0.85, 0.85))
            c.setLineWidth(0.7)
            c.line(cur_x, y, cur_x + cur_w, y)
            y -= 8
            c.setFont(base_font, 11)

            upper_title = title.upper()

            if upper_title == "DETAILS":
                for raw in body_lines:
                    s = _sanitize_ascii(raw).strip()
                    if not s:
                        y -= line_h * 0.7
                        continue
                    if s.lower().startswith("contact:"):
                        continue
                    if y < bottom + line_h:
                        c.showPage(); y = page_h - margin; c.setFont(base_font, 11)
                    if ":" in s:
                        label, value = s.split(":", 1)
                        c.setFont(bold_font, 10)
                        c.drawString(cur_x, y, label.strip().upper())
                        c.setFont(base_font, 10)
                        c.drawString(cur_x + 90, y, value.strip())
                        y -= line_h * 0.85
                    else:
                        c.setFont(base_font, 10)
                        y = _wrap_draw(c, s, cur_x, y, cur_w, line_h * 0.9, base_font, 10, bottom)
                y -= 4
                c.setFont(base_font, 11)
            elif upper_title == "SKILLS":
                items = [
                    _sanitize_ascii(l).lstrip("- ").strip()
                    for l in body_lines if _sanitize_ascii(l).strip()
                ]
                # If comma-separated single line, split by comma
                if len(items) <= 1 and items:
                    items = [p.strip() for p in items[0].split(',') if p.strip()]
                if not items:
                    items = ["—"]
                # Single narrow column bullets (pure black)
                for item in items:
                    if y < bottom + line_h:
                        c.showPage(); y = page_h - margin; c.setFont(base_font, 11)
                    bx, by = cur_x, y + 4
                    c.setFillColor(colors.black)
                    c.circle(bx + 2.5, by, 1.5, fill=1, stroke=0)
                    c.setFillColor(colors.black)
                    y = _wrap_draw(c, item, cur_x + 10, y, cur_w - 10, line_h, base_font, 11, bottom)
                y -= 2
            else:
                # Render bullets when lines start with '-' else wrap paragraph
                block = [l for l in body_lines if l is not None]
                for raw in block:
                    s = _sanitize_ascii(raw).rstrip()
                    if s.startswith('- '):
                        # draw bullet line
                        if y < bottom + line_h:
                            c.showPage(); y = page_h - margin; c.setFont(base_font, 11)
                        bx, by = cur_x, y + 4
                        c.setFillColor(colors.black)
                        c.circle(bx + 2.5, by, 1.5, fill=1, stroke=0)
                        c.setFillColor(colors.black)
                        y = _wrap_draw(c, s[2:].strip(), cur_x + 10, y, cur_w - 10, line_h, base_font, 11, bottom)
                    elif s.strip() == "":
                        y -= line_h
                    else:
                        y = _wrap_draw(c, s, cur_x, y, cur_w, line_h, base_font, 11, bottom)
                y -= 6

        # Render sections if any content
        # Left column content
        cur_x, cur_w = left_x, left_w
        left_y_start = y
        y = left_y_start
        for key in ("DETAILS", "SKILLS"):
            body = sections.get(key, [])
            if any(s.strip() for s in body):
                section(key, body)

        # Right column
        cur_x, cur_w = right_x, right_w
        y = left_y_start
        for key in ("SUMMARY", "EXPERIENCE", "PROJECTS", "EDUCATION"):
            body = sections.get(key, [])
            if any(s.strip() for s in body):
                section(key, body)

        c.save()
