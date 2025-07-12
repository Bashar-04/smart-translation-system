
# 📄 Smart Translation System – Jordan Customs

An AI-powered desktop application for translating text extracted from images and PDFs – entirely offline. Designed for government use, especially customs environments, where security and speed are crucial.

## 🚀 Features
- 📤 Extracts text from images and PDFs
- 🔍 Automatically detects the original language
- 🌍 Translates between multiple languages
- 🖥️ Simple and bilingual user interface (Arabic/English)
- 💾 Option to save translated results
- ✅ Works completely offline (no internet required)

## 🧠 AI Used
- **EasyOCR** for Optical Character Recognition (OCR)
- **langdetect** for automatic language detection
- **Argos Translate** for offline neural machine translation (Marian-NMT)

## 🧩 Tech Stack
- `Python`, `customtkinter`, `easyocr`, `pdfplumber`, `langdetect`, `argos-translate`, `torch`, `opencv-python`, `pillow`, `numpy`

## 🗂️ Project Structure
```
project/
│
├── main.py                  ← GUI entry point
├── ocr_utils.py             ← Image OCR logic
├── pdf_utils.py             ← PDF text extraction
├── translator.py            ← Language detection & translation
├── model_installer.py       ← Installs .argosmodel translation files
├── ui_labels.py             ← Handles UI language switching
├── run_app.bat              ← Batch file to launch the app easily
├── requirements.txt         ← Required Python libraries
└── ln/                      ← Folder for translation models (.argosmodel)
```

---

### 🔤 Language Models (Argos Translate)

This project uses **offline translation models** provided by [Argos OpenTech](https://www.argosopentech.com/argospm/index/).

To enable translation between your desired languages:

1. Visit the official model repository:  
   👉 https://www.argosopentech.com/argospm/index/

2. Download the `.argosmodel` files you need (e.g. `en_ar.argosmodel`, `en_fr.argosmodel`, etc.)

3. Create a folder named `ln/` inside the project directory (if not already present).

4. Place the downloaded `.argosmodel` files inside that `ln/` folder.

5. Run the following command to install them:

   ```bash
   python model_installer.py
   ```

💡 Once installed, the models can be used **completely offline**, without internet access.
