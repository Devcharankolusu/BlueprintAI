import re
from markupsafe import Markup
from flask import Flask, render_template, request, send_file
from services.granite_service import test_connection
from services.pdf_generator import create_pdf
from bs4 import BeautifulSoup

app = Flask(__name__)

latest_report = {}

def parse_sections(text):

    sections = {}

    current_heading = None
    current_content = []

    for line in text.splitlines():

        line = line.strip()

        if line.startswith("SECTION:"):

            if current_heading:
                sections[current_heading] = "\n".join(current_content).strip()

            current_heading = line.replace("SECTION:", "").strip()
            current_content = []

        else:

            if current_heading:
                current_content.append(line)

    if current_heading:
        sections[current_heading] = "\n".join(current_content).strip()

    return sections
def format_content(text):

    if not text:
        return ""

    # Bold (**text**)
    text = re.sub(r"\*\*(.*?)\*\*", r"<strong>\1</strong>", text)

    lines = text.split("\n")

    html = ""

    in_list = False

    for line in lines:

        line = line.strip()

        if not line:
            continue

        if line.startswith("-"):

            if not in_list:

                html += "<ul>"

                in_list = True

            html += f"<li>{line[1:].strip()}</li>"

        else:

            if in_list:

                html += "</ul>"

                in_list = False

            html += f"<p>{line}</p>"

    if in_list:

        html += "</ul>"

    return Markup(html)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():

    idea = request.form["idea"]
    industry = request.form["industry"]
    budget = request.form["budget"]
    country = request.form["country"]
    stage = request.form["stage"]
    ai_level = request.form["ai_level"]
    audience = request.form["audience"]

    prompt = f"""
You are an experienced startup consultant, business strategist, venture capitalist, and product manager.

Your task is to create a professional startup blueprint.

STRICT RULES:
- Do NOT write Python code.
- Do NOT explain AI.
- Do NOT mention language models.
- Do NOT use placeholders.
- Generate realistic content.
- Give the startup a creative name.
- Think like an investor.

Startup Details

Startup Idea:
{idea}

Industry:
{industry}

Country:
{country}

Business Stage:
{stage}

AI Integration:
{ai_level}

Budget:
{budget}

Target Audience:
{audience}

Generate the report with EXACTLY these headings.

SECTION: Startup Name

SECTION: Executive Summary

SECTION: Problem Statement

SECTION: Proposed Solution

SECTION: Unique Selling Proposition

SECTION: Target Audience

SECTION: Market Analysis

SECTION: Competitor Analysis

SECTION: Revenue Model

SECTION: Marketing Strategy

SECTION: SWOT Analysis

SECTION: Risk Analysis

SECTION: AI Features Recommendation

SECTION: Recommended Technology Stack

SECTION: Budget Allocation

SECTION: Funding Recommendation

SECTION: Six-Month Roadmap

SECTION: Future Expansion

Write professionally.

Use bullet points whenever appropriate.

Do not leave any section empty.
"""

    result = test_connection(prompt)

    sections = parse_sections(result)

    # Extract startup name BEFORE formatting sections
    startup_name = ""
    tagline = ""

    if "Startup Name" in sections:

        startup = sections["Startup Name"]

        startup = BeautifulSoup(startup, "html.parser").get_text()

        startup = (
            startup.replace("**", "")
                .replace("*", "")
                .replace("- ", "")
                .replace("•", "")
                .replace("Name:", "")
                .strip()
        )

        if "Tagline:" in startup:

            parts = startup.split("Tagline:", 1)

            startup_name = parts[0].strip(" -:")

            tagline = parts[1].strip()

        elif "-" in startup and len(startup.split("-", 1)[0].split()) <= 5:

            parts = startup.split("-", 1)

            startup_name = parts[0].strip()

            tagline = parts[1].strip()

        else:

            startup_name = startup

            tagline = ""

        sections["Startup Name"] = startup_name

    # NOW format all the remaining sections
    for key in sections:
        if key != "Startup Name":
            sections[key] = format_content(sections[key])

    if "Startup Name" in sections:
        startup = sections["Startup Name"]
        # Remove markdown and unwanted symbols
        startup = (
            startup.replace("**", "")
                   .replace("*", "")
                   .replace("- ", "")
                   .replace("•", "")
                   .replace("Name:", "")
                   .strip()
        )

        # If AI includes a tagline in the same section
        if "Tagline:" in startup:

            parts = startup.split("Tagline:", 1)

            startup_name = parts[0].strip(" -:")

            tagline = parts[1].strip()

        elif "-" in startup and len(startup.split("-", 1)[0].split()) <= 5:

            # Handles formats like:
            # HealthCamp AI - Smarter Healthcare...
            parts = startup.split("-", 1)

            startup_name = parts[0].strip()

            tagline = parts[1].strip()

        else:

            startup_name = startup.strip()

            tagline = ""
        sections["Startup Name"] = startup_name
    global latest_report

    latest_report = {
        "startup_name": startup_name,
        "tagline": tagline,
        "sections": sections
    }

    return render_template(
        "result.html",
        sections=sections,
        startup_name=startup_name,
        tagline=tagline,
        industry=industry,
        budget=budget,
        country=country,
        stage=stage,
        audience=audience
    )
    

@app.route("/download_pdf")
def download_pdf():

    if not latest_report:
        return "No blueprint generated yet."

    filename = "Startup_Blueprint.pdf"

    create_pdf(
        filename,
        latest_report["startup_name"],
        latest_report["tagline"],
        latest_report["sections"]
    )

    return send_file(
        filename,
        as_attachment=True
    )

if __name__ == "__main__":
    app.run(debug=True)