from langdetect import detect
from argostranslate.translate import get_installed_languages

def detect_and_translate(text, target_lang_code):
    try:
        source_lang_code = detect(text)
        installed_languages = get_installed_languages()
        from_lang = next((lang for lang in installed_languages if lang.code == source_lang_code), None)
        to_lang = next((lang for lang in installed_languages if lang.code == target_lang_code), None)
        if from_lang and to_lang:
            translation = from_lang.get_translation(to_lang)
            return source_lang_code, translation.translate(text)
        else:
            return source_lang_code, "❌ Language not installed."
    except Exception as e:
        return "??", f"❌ Translation error:\n{e}"