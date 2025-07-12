import pdfplumber

def extract_text_from_pdf(path):
    try:
        text = ''
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + '\n'
        return text.strip()
    except Exception as e:
        return f"❌ Error extracting PDF text:\n{e}"