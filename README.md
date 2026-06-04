# ResumeIQ - AI Resume Intelligence Platform

## Overview

ResumeIQ is an AI-powered Resume Intelligence Platform that transforms traditional resume parsing into an interactive career analytics dashboard.

The platform analyzes uploaded resumes, evaluates ATS compatibility, measures job-role fit, extracts skills, generates SWOT insights, and produces professional PDF reports.

Built using Python, Streamlit, NLP, and data visualization technologies, ResumeIQ provides candidates with actionable recommendations to improve their resumes and increase their chances of landing interviews.

---

## Features

### Resume Parsing

* PDF Resume Upload
* Multi-page Resume Support
* Automatic Text Extraction

### Information Extraction

* Email Detection
* Phone Number Detection
* Skills Extraction
* Education Detection
* Experience Detection
* Projects & Certifications Support

### ATS Analysis

* ATS Readiness Score
* Missing Section Detection
* Keyword Analysis
* Resume Improvement Recommendations

### Resume Scoring

* Overall Resume Score
* Category-wise Evaluation
* ATS Compatibility Assessment

### Skill Intelligence Dashboard

* Skill Categorization
* Programming Skills Analysis
* AI/ML Skills Analysis
* Web Development Skills Analysis
* Cloud & DevOps Skills Analysis
* Tool Proficiency Analysis

### Interactive Visualizations

* Skill Distribution Pie Chart
* Skill Category Bar Chart
* Resume Score Radar Chart
* Keyword Frequency Analysis

### SWOT Analysis

* Strengths
* Weaknesses
* Opportunities
* Threats

### Job Role Matching

Supports roles such as:

* AI Engineer
* Machine Learning Engineer
* Data Scientist
* Software Engineer
* Full Stack Developer
* Frontend Developer
* Backend Developer
* Cloud Engineer
* DevOps Engineer
* Cybersecurity Analyst
* Product Manager
* AI Intern
* Software Engineering Intern
* And more

### Professional Reporting

* Executive Summary Generation
* Professional PDF Report Export
* Downloadable Candidate Insights

---

## Technology Stack

### Frontend

* Streamlit

### Backend

* Python

### NLP

* spaCy

### PDF Processing

* pdfplumber

### Data Analysis

* Pandas

### Data Visualization

* Plotly

### Report Generation

* FPDF

---

## Project Structure

resume_intelligence_platform/

├── app.py

├── analyzer/

│ ├── ats_analyzer.py

│ ├── role_matcher.py

│ ├── scoring_engine.py

│ ├── skill_analyzer.py

│ └── swot_analyzer.py

├── parser/

│ ├── pdf_parser.py

│ └── information_extractor.py

├── dashboard/

│ ├── charts.py

│ └── components.py

├── reports/

│ └── pdf_report.py

├── data/

│ ├── skills_db.json

│ └── job_roles.json

├── assets/

│ ├── logo.png

│ └── style.css

├── requirements.txt

└── README.md

---

## Installation

Clone the repository

```bash
git clone https://github.com/yourusername/resumeiq.git
cd resumeiq
```

Create a virtual environment

```bash
python -m venv venv
```

Activate the environment

Windows

```bash
venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Download spaCy model

```bash
python -m spacy download en_core_web_sm
```

Run the application

```bash
streamlit run app.py
```

---

## Future Enhancements

* LLM-powered resume recommendations
* LinkedIn profile analysis
* Resume comparison tool
* AI-generated cover letters
* Recruiter analytics dashboard
* Interview readiness assessment
* Resume benchmarking against job descriptions

---

## Author

Baani

Bachelor of Engineering (Computer Science Engineering - AI & ML)

Chandigarh University

---

## License

This project is developed for educational and portfolio purposes.
