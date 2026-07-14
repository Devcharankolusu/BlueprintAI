from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer
)

from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.colors import HexColor


def create_pdf(filename, startup_name, tagline, sections):

    doc = SimpleDocTemplate(filename)

    styles = getSampleStyleSheet()

    title_style = styles["Title"]
    title_style.alignment = TA_CENTER
    title_style.textColor = HexColor("#0F62FE")

    heading_style = styles["Heading2"]
    heading_style.textColor = HexColor("#0F62FE")

    normal_style = styles["BodyText"]

    story = []

    # -------------------------
    # Title
    # -------------------------

    story.append(
        Paragraph("BlueprintAI", title_style)
    )

    story.append(Spacer(1, 12))

    story.append(
        Paragraph(startup_name, styles["Heading1"])
    )

    if tagline:
        story.append(
            Paragraph(tagline, styles["Italic"])
        )

    story.append(Spacer(1, 20))

    # -------------------------
    # Sections
    # -------------------------

    for heading, content in sections.items():

        if heading == "Startup Name":
            continue

        story.append(
            Paragraph(heading, heading_style)
        )

        story.append(Spacer(1, 6))

        # Remove HTML tags
        clean_text = str(content)

        clean_text = clean_text.replace("<p>", "")
        clean_text = clean_text.replace("</p>", "<br/>")

        clean_text = clean_text.replace("<ul>", "")
        clean_text = clean_text.replace("</ul>", "")

        clean_text = clean_text.replace("<li>", "• ")
        clean_text = clean_text.replace("</li>", "<br/>")

        clean_text = clean_text.replace("<strong>", "<b>")
        clean_text = clean_text.replace("</strong>", "</b>")

        story.append(
            Paragraph(clean_text, normal_style)
        )

        story.append(Spacer(1, 18))

    doc.build(story)