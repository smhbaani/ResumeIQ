import pdfplumber

def extract_text_from_pdf(pdf_file):

    full_text = ""

    try:
        with pdfplumber.open(pdf_file) as pdf:

            for page in pdf.pages:
                text = page.extract_text()

                if text:
                    full_text += text + "\n"

    except Exception as e:
        return ""

    return full_text