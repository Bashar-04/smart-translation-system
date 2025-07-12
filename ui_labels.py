def update_ui_language_ar(controls):
    controls["title"].configure(text="📄 نظام الترجمة الذكي - الجمارك الأردنية")
    controls["open_button"].configure(text="📂 اختر صورة أو ملف PDF")
    controls["lang_label"].configure(text="🌐 اللغة المكتشفة:")
    controls["original_label"].configure(text="📝 النص المُستخرج:")
    controls["translated_label"].configure(text="🌍 الترجمة:")
    controls["save_button"].configure(text="💾 حفظ الترجمة")
    controls["lang_title"].configure(text="🌍 اختر لغة الترجمة:")
    controls["ui_lang_title"].configure(text="🖥️ اختر لغة الواجهة:")

def update_ui_language_en(controls):
    controls["title"].configure(text="📄 Smart Translation System - Jordan Customs")
    controls["open_button"].configure(text="📂 Select Image or PDF File")
    controls["lang_label"].configure(text="🌐 Detected Language:")
    controls["original_label"].configure(text="📝 Extracted Text:")
    controls["translated_label"].configure(text="🌍 Translated Text:")
    controls["save_button"].configure(text="💾 Save Translation")
    controls["lang_title"].configure(text="🌍 Choose Translation Language:")
    controls["ui_lang_title"].configure(text="🖥️ UI Language:")