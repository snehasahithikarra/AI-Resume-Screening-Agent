import PyPDF2

def extract_text_from_pdf(uploaded_file):
    """
    Extract text from an uploaded PDF resume.
    """

    text = ""

    try:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)

        for page in pdf_reader.pages:
            extracted = page.extract_text()

            if extracted:
                text += extracted + "\n"

    except Exception as e:
        text = f"Error reading PDF: {e}"

    return text
