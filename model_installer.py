import os
from argostranslate import package

# المسار إلى مجلد 'ln' الموجود داخل نفس مجلد المشروع
models_folder = os.path.join(os.path.dirname(__file__), "ln")

# تثبيت كل الملفات التي تنتهي بـ .argosmodel
for filename in os.listdir(models_folder):
    if filename.endswith(".argosmodel"):
        file_path = os.path.join(models_folder, filename)
        try:
            package.install_from_path(file_path)
            print(f"✅ تم تثبيت: {filename}")
        except Exception as e:
            print(f"❌ خطأ في تثبيت {filename}: {e}")
