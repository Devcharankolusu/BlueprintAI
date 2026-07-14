# BlueprintAI
# AI Startup Blueprint Generator

An AI-powered web application that helps aspiring entrepreneurs transform startup ideas into comprehensive business blueprints using **IBM watsonx.ai** and **IBM Granite Models**.

---

## 📌 Project Overview

The AI Startup Blueprint Generator simplifies business planning by analyzing user-provided startup ideas and automatically generating structured, investor-ready business plans. The application leverages IBM Granite foundation models to produce intelligent, context-aware, and personalized startup blueprints.

---

## ✨ Features

- 💡 Startup Idea Analysis
- 📄 AI-Generated Business Blueprint
- 📈 Business Model & Revenue Strategy
- 🎯 Target Audience Identification
- 📢 Marketing Strategy Suggestions
- 💰 Financial & Growth Recommendations
- 📥 Download Blueprint as PDF
- 🤖 Powered by IBM Granite Models

---

## 🛠️ Technologies Used

- Python
- Flask
- HTML5
- CSS3
- JavaScript
- IBM watsonx.ai
- IBM Granite 3.3-8B-Instruct
- IBM Cloud Lite

---

## 📂 Project Structure

```
BlueprintAI/
│
├── prompts/
│   └── blueprint_prompt.txt
│
├── services/
│   ├── granite_service.py
│   └── pdf_generator.py
│
├── Static/
│   ├── images/
│   ├── style.css
│   └── result.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── requirements.txt
├── Startup_Blueprint.pdf
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### Clone the Repository

```bash
git clone https://github.com/Devcharankolusu/BlueprintAI.git
```

### Navigate to the Project

```bash
cd BlueprintAI
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

**Windows**

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## 📸 Application Workflow

1. User enters startup details.
2. Flask backend processes the request.
3. Prompt Engineering structures the input.
4. IBM watsonx.ai sends the request to IBM Granite.
5. Granite generates a comprehensive startup blueprint.
6. Results are displayed and can be downloaded as a PDF.

---

## 📄 Output

The generated startup blueprint includes:

- Executive Summary
- Problem Statement
- Proposed Solution
- Target Audience
- Business Model
- Revenue Model
- Marketing Strategy
- Implementation Roadmap
- Growth Recommendations

---

## 🎯 Future Enhancements

- Market Trend Analysis
- Competitor Analysis
- Financial Forecasting
- Investor Pitch Deck Generation
- Multilingual Support
- Cloud Deployment on IBM Cloud

---

## 👨‍💻 Developed By

**Kolusu Devi Charan**

Department of Computer Science and Engineering

Sir C. R. Reddy College of Engineering

---

## 📜 License

This project is developed for the **IBM SkillsBuild AICTE Internship Program** under the IBM University Engagement initiative.
