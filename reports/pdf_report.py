from fpdf import FPDF
def generate_pdf_report(
        filename,
        resume_data,
        overall_score,
        ats_score,
        role_match,
        recommendations
):
    pdf = FPDF()

    pdf.add_page()

    pdf.set_font("Times", "B", 20)
    
    pdf.cell(
        0,
        10,
        "ResumeIQ Intelligence Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    pdf.set_font("Times", "", 12)

    pdf.cell(
        0,
        10,
        f"Email: {resume_data.get('email')}",
        ln=True
    )

    pdf.cell(
        0,
        10,
        f"Phone: {resume_data.get('phone')}",
        ln=True
    )

    pdf.ln(5)

    pdf.cell(
        0,
        10,
        f"Resume Score: {overall_score}/100",
        ln=True
    )

    pdf.cell(
        0,
        10,
        f"ATS Score: {ats_score}/100",
        ln=True
    )

    pdf.cell(
        0,
        10,
        f"Role Match: {role_match}%",
        ln=True
    )

    pdf.ln(10)

    pdf.set_font("Arial", "B", 14)

    pdf.cell(
        0,
        10,
        "Recommendations",
        ln=True
    )

    pdf.set_font("Arial", "", 12)

    for item in recommendations:
        pdf.multi_cell(
            0,
            8,
            f"- {item}"
        )

    pdf.output(filename)