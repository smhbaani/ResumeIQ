import streamlit as st
import pandas as pd

from parser.pdf_parser import extract_text_from_pdf
from parser.information_extractor import extract_resume_data

from analyzer.ats_analyzer import analyze_ats
from analyzer.scoring_engine import calculate_resume_score
from analyzer.skill_analyzer import analyze_skills
from analyzer.swot_analyzer import generate_swot
from analyzer.role_matcher import role_match

from reports.pdf_report import generate_pdf_report

from dashboard.charts import (
    create_skill_pie,
    create_skill_bar,
    create_radar_chart,
    create_keyword_chart
)

from dashboard.components import (
    metric_card,
    section_header,
    swot_card,
    recommendation_box
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="ResumeIQ",
    page_icon="📄",
    layout="wide"
)

# ==========================================================
# LOAD CSS
# ==========================================================

try:
    with open("assets/style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )
except:
    pass

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("## ResumeIQ")

    st.markdown("---")

    st.info(
        "Upload a resume PDF and receive ATS analysis, role matching, SWOT insights and skill intelligence."
    )
# ==========================================================
# HEADER
# ==========================================================

col1, col2 = st.columns([1, 5])

with col1:
    st.image("assets/logo.png", width=120)

with col2:
    st.title("ResumeIQ")
    st.caption("AI Resume Intelligence Platform")

st.markdown("---")

# ==========================================================
# FILE UPLOAD
# ==========================================================
st.subheader(
    "Target Role"
)

selected_role = st.selectbox(
    "Select the job role you're applying for",
    [
        # AI & Data
        "AI Engineer",
        "Machine Learning Engineer",
        "Data Scientist",
        "Data Analyst",
        "Business Analyst",
        "Computer Vision Engineer",
        "NLP Engineer",

        # Software Development
        "Software Engineer",
        "Full Stack Developer",
        "Frontend Developer",
        "Backend Developer",
        "Python Developer",
        "Java Developer",

        # Cloud & DevOps
        "Cloud Engineer",
        "DevOps Engineer",
        "Site Reliability Engineer",
        "MLOps Engineer",

        # Cybersecurity
        "Cybersecurity Analyst",
        "Ethical Hacker",
        "Security Engineer",

        # Mobile Development
        "Android Developer",
        "iOS Developer",
        "Flutter Developer",

        # Product & Design
        "Product Manager",
        "UI/UX Designer",

        # Emerging Tech
        "Blockchain Developer",
        "AR/VR Developer",

        # Student Roles
        "AI Intern",
        "Software Engineering Intern",
        "Data Science Intern",
        "Research Intern"
    ]
)

uploaded_file = st.file_uploader(
    "Upload Resume (PDF)",
    type=["pdf"]
)

# ==========================================================
# MAIN LOGIC
# ==========================================================

if uploaded_file:

    with st.spinner("Analyzing Resume..."):

        resume_text = extract_text_from_pdf(uploaded_file)

        resume_data = extract_resume_data(resume_text)

        skill_analysis = analyze_skills(resume_text)

        ats_result = analyze_ats(resume_data)

        overall_score, category_scores = calculate_resume_score(
            resume_data
        )

        swot = generate_swot(resume_data)

        try:
            match_percent, missing_skills = role_match(
            skill_analysis["skills"],
            selected_role
    )
        except:
            match_percent = 0
            missing_skills = []
        

    st.success("Analysis Complete")

    # ======================================================
    # TOP METRICS
    # ======================================================

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Resume Score",
            f"{overall_score}/100"
        )

    with col2:
        st.metric(
            "ATS Score",
            f"{ats_result['score']}/100"
        )

    with col3:
        st.metric(
            "Role Match",
            f"{match_percent}%"
        )

    with col4:
        st.metric(
            "Skills Found",
            len(skill_analysis["skills"])
        )

    st.markdown("---")

    # ======================================================
    # TABS
    # ======================================================

    tab1, tab2, tab3, tab4, tab5 = st.tabs([
        "Overview",
        "ATS Analysis",
        "Skill Intelligence",
        "SWOT Analysis",
        "Executive Report"
    ])

    # ======================================================
    # OVERVIEW TAB
    # ======================================================

    with tab1:

        section_header("Candidate Information")

        c1, c2 = st.columns(2)

        with c1:
            st.write(
                "**Email:**",
                resume_data.get("email", "Not Found")
            )

        with c2:
            st.write(
                "**Phone:**",
                resume_data.get("phone", "Not Found")
            )

        st.markdown("### Skills")

        if skill_analysis["skills"]:
            st.write(skill_analysis["skills"])
        else:
            st.warning("No skills detected")

        st.markdown("### Education")

        st.write(
            resume_data.get("education", [])
        )

        st.markdown("### Experience")

        st.write(
            resume_data.get("experience", [])
        )

        st.markdown("### Resume Score Breakdown")

        radar = create_radar_chart(
            category_scores
        )

        st.plotly_chart(
            radar,
            use_container_width=True
        )

    # ======================================================
    # ATS TAB
    # ======================================================

    with tab2:

        section_header("ATS Compatibility")

        st.progress(
            ats_result["score"] / 100
        )

        st.metric(
            "ATS Score",
            ats_result["score"]
        )

        st.markdown("### Recommendations")

        if ats_result["recommendations"]:

            for rec in ats_result["recommendations"]:
                recommendation_box(rec)

        else:
            st.success(
                "Excellent ATS Readiness"
            )

        st.markdown("### Missing Skills")

        if missing_skills:
            st.warning(
                ", ".join(missing_skills)
            )

    # ======================================================
    # SKILL TAB
    # ======================================================

    with tab3:

        section_header("Skill Intelligence")

        col1, col2 = st.columns(2)

        with col1:

            pie_chart = create_skill_pie(
                skill_analysis["distribution"]
            )

            st.plotly_chart(
                pie_chart,
                use_container_width=True
            )

        with col2:

            bar_chart = create_skill_bar(
                skill_analysis["distribution"]
            )

            st.plotly_chart(
                bar_chart,
                use_container_width=True
            )

        st.markdown("### Keyword Frequency")

        if skill_analysis["frequent"]:

            keyword_chart = create_keyword_chart(
                skill_analysis["frequent"]
            )

            st.plotly_chart(
                keyword_chart,
                use_container_width=True
            )

        st.markdown(
            f"### Skill Maturity Score: {skill_analysis['maturity_score']}/100"
        )

        st.progress(
            skill_analysis["maturity_score"] / 100
        )

        st.markdown("### Recommended Skills")

        st.write(
            skill_analysis["recommendations"]
        )

    # ======================================================
    # SWOT TAB
    # ======================================================

    with tab4:

        section_header("SWOT Analysis")

        col1, col2 = st.columns(2)

        with col1:

            swot_card(
                "Strengths",
                swot["strengths"]
            )

            swot_card(
                "Opportunities",
                swot["opportunities"]
            )

        with col2:

            swot_card(
                "Weaknesses",
                swot["weaknesses"]
            )

            swot_card(
                "Threats",
                swot["threats"]
            )

    # ======================================================
    # EXECUTIVE REPORT TAB
    # ======================================================

    with tab5:

        section_header("Executive Summary")

        report = f"""
    RESUMEIQ AI INTELLIGENCE REPORT

    ========================================

    CANDIDATE INFORMATION
    ----------------------------------------

    Email:
    {resume_data.get('email')}

    Phone:
    {resume_data.get('phone')}

    ========================================

    PERFORMANCE SCORES
    ----------------------------------------

    Resume Score:
    {overall_score}/100

    ATS Score:
    {ats_result['score']}/100

    Role Match:
    {match_percent}%

    ========================================

    SKILLS IDENTIFIED
    ----------------------------------------

    {', '.join(skill_analysis['skills'])}

    ========================================

    RECOMMENDED SKILLS
    ----------------------------------------

    {', '.join(skill_analysis['recommendations'])}

    ========================================

    ATS RECOMMENDATIONS
    ----------------------------------------

    {chr(10).join(ats_result['recommendations'])}

    ========================================

    END OF REPORT
    """

        st.text_area(
            "Generated Report",
            report,
            height=350
        )

        # ==========================================
        # GENERATE PDF
        # ==========================================

        pdf_path = "reports/resume_report.pdf"

        generate_pdf_report(
            filename=pdf_path,
            resume_data=resume_data,
            overall_score=overall_score,
            ats_score=ats_result["score"],
            role_match=match_percent,
            recommendations=ats_result["recommendations"]
        )

        # ==========================================
        # DOWNLOAD PDF BUTTON
        # ==========================================

        try:

            with open(pdf_path, "rb") as pdf_file:

                st.download_button(
                    label="📄 Download Professional PDF Report",
                    data=pdf_file,
                    file_name="ResumeIQ_Report.pdf",
                    mime="application/pdf"
                )

        except Exception as e:

            st.error(
                f"Unable to generate PDF: {e}"
            )