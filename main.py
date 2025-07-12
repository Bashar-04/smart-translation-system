import customtkinter as ctk
from tkinter import filedialog, messagebox, scrolledtext
import warnings

from ocr_utils import extract_text_from_image
from pdf_utils import extract_text_from_pdf
from translator import detect_and_translate
from ui_labels import update_ui_language_ar, update_ui_language_en

warnings.filterwarnings("ignore", message=".*pin_memory.*")

def update_ui_language():
    lang = ui_lang_var.get()
    controls = {
        "title": title,
        "open_button": open_button,
        "lang_label": lang_label,
        "original_label": original_label,
        "translated_label": translated_label,
        "save_button": save_button,
        "lang_title": lang_title,
        "ui_lang_title": ui_lang_title,
    }
    if lang == "ar":
        update_ui_language_ar(controls)
    else:
        update_ui_language_en(controls)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Image and PDF files", "*.png *.jpg *.jpeg *.pdf")])
    if not file_path:
        return
    extracted_text = ""
    if file_path.lower().endswith(('.png', '.jpg', '.jpeg')):
        extracted_text = extract_text_from_image(file_path)
    elif file_path.lower().endswith('.pdf'):
        extracted_text = extract_text_from_pdf(file_path)
    else:
        messagebox.showerror("خطأ", "صيغة الملف غير مدعومة.")
        return

    original_text_box.delete("1.0", "end")
    translated_text_box.delete("1.0", "end")
    original_text_box.insert("end", extracted_text)

    if extracted_text.strip() and not extracted_text.startswith("❌"):
        target_lang = lang_var.get()
        lang, translated = detect_and_translate(extracted_text, target_lang)
        translated_text_box.insert("end", translated)
        lang_label.configure(text=f"🌐 اللغة المكتشفة: {lang}" if ui_lang_var.get() == "ar" else f"🌐 Detected Language: {lang}")
    else:
        lang_label.configure(text="🌐 اللغة المكتشفة: لا يوجد نص" if ui_lang_var.get() == "ar" else "🌐 No text detected")
        translated_text_box.insert("end", "❌ لا يمكن الترجمة." if ui_lang_var.get() == "ar" else "❌ Cannot translate.")

def save_translation():
    text = translated_text_box.get("1.0", "end").strip()
    if not text:
        messagebox.showwarning("تحذير", "لا يوجد ترجمة." if ui_lang_var.get() == "ar" else "No translation to save.")
        return
    path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if path:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        messagebox.showinfo("تم", "✅ تم الحفظ بنجاح." if ui_lang_var.get() == "ar" else "✅ Translation saved successfully.")

# ===== واجهة المستخدم =====
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("📄 الجمارك الأردنية - نظام الترجمة")
app.geometry("900x700")
app.configure(bg="#1f1f1f")

ui_lang_var = ctk.StringVar(value="ar")
lang_var = ctk.StringVar(value="ar")

title = ctk.CTkLabel(app, text="", font=("Arial", 22, "bold"), text_color="#00C9A7", bg_color="#1f1f1f")
title.pack(pady=10)

top_controls_frame = ctk.CTkFrame(app, fg_color="#2c2c2c")
top_controls_frame.pack(pady=5)

ui_lang_title = ctk.CTkLabel(top_controls_frame, text="", font=("Arial", 13), text_color="#ffffff")
ui_lang_title.grid(row=0, column=0, padx=5)

ui_lang_menu = ctk.CTkComboBox(top_controls_frame, variable=ui_lang_var, values=["ar", "en"],
                               command=lambda _: update_ui_language(), width=100)
ui_lang_menu.grid(row=0, column=1, padx=5)

lang_title = ctk.CTkLabel(top_controls_frame, text="", font=("Arial", 13), text_color="#ffffff")
lang_title.grid(row=0, column=2, padx=(20, 5))

lang_menu = ctk.CTkComboBox(top_controls_frame, variable=lang_var, values=["ar", "en", "fr", "de", "ru"], width=120)
lang_menu.grid(row=0, column=3, padx=5)

open_button = ctk.CTkButton(app, text="", command=open_file,
                            fg_color="#0078D4", hover_color="#005A9E", text_color="white", width=200)
open_button.pack(pady=15)

lang_label = ctk.CTkLabel(app, text="", font=("Arial", 14), text_color="#ffffff")
lang_label.pack(pady=5)

original_label = ctk.CTkLabel(app, text="", text_color="#ffffff")
original_label.pack()
original_text_box = scrolledtext.ScrolledText(app, height=8, wrap="word", bg="#f2f2f2", fg="#000000", insertbackground="#000000")
original_text_box.pack(padx=10, pady=5, fill="both", expand=True)

translated_label = ctk.CTkLabel(app, text="", text_color="#ffffff")
translated_label.pack()
translated_text_box = scrolledtext.ScrolledText(app, height=8, wrap="word", bg="#f2f2f2", fg="#000000", insertbackground="#000000")
translated_text_box.pack(padx=10, pady=5, fill="both", expand=True)

save_button = ctk.CTkButton(app, text="", command=save_translation,
                            fg_color="#28A745", hover_color="#218838", text_color="white", width=200)
save_button.pack(pady=15)

if __name__ == "__main__":
    update_ui_language()
    app.mainloop()
