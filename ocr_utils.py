import easyocr
from langdetect import detect

reader_ar = easyocr.Reader(['ar', 'en', 'fa', 'ur', 'ug'], gpu=False)
reader_ru = easyocr.Reader(['ru', 'rs_cyrillic', 'be', 'bg', 'uk', 'mn', 'en'], gpu=False)
reader_general = easyocr.Reader(['en', 'fr', 'de'], gpu=False)

def extract_text_from_image(path):
    try:
        text = " ".join(reader_general.readtext(path, detail=0))
        if not text.strip():
            return ""
        lang = detect(text)
        if lang == 'ar':
            text = " ".join(reader_ar.readtext(path, detail=0))
        elif lang == 'ru':
            text = " ".join(reader_ru.readtext(path, detail=0))
        return text.strip()
    except Exception as e:
        return f"❌ Error extracting image text:\n{e}"