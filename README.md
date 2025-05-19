
# 📚 InsightScope – AI-Powered Research Assistant

**InsightScope** is a streamlined, smart research assistant built with OpenAI and OCR tech. It lets users upload documents, extract key insights, summarize text, and detect bias — all from PDFs, images, or URLs.

---

## 🚀 Features

- ✅ Upload **PDF**, **Image**, or **Text** files
- 🌐 Paste a **news article URL**
- 🧠 Extract text using **Tesseract OCR**
- ✍️ Summarize content using **GPT-4o**
- 🧠 Detect **bias** in the content (positive/negative/neutral)
- 💾 Download extracted text

---

## 📦 Installation

### 1. Clone this repository
```bash
git clone https://github.com/yourusername/insightscope.git
cd insightscope
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR

#### Windows:
Download from [UB Mannheim build](https://github.com/UB-Mannheim/tesseract/wiki)

Set path manually in Python if needed:
```python
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
```

### 4. Add `.env` file
Create a `.env` file with your OpenAI key:

```
OPENAI_API_KEY=your_openai_key_here
```

---

## 🧠 Usage

Start the app using Streamlit:

```bash
streamlit run main.py
```

Then visit `http://localhost:8501` in your browser.

---

## 🛠 Tech Stack

- `Streamlit` for UI
- `OpenAI GPT-4o` via LangChain
- `Pytesseract` + `Pillow` for image OCR
- `PyMuPDF` (fitz) for PDF parsing
- `newspaper3k` for news URL content extraction

---

## 📁 Project Structure

```
.
├── main.py
├── requirements.txt
├── README.md
├── .env.example
├── assets/
│   └── insightscope.jpg
```

---

## 🔒 Notes

- This app uses GPT-4o via OpenAI API.
- Do **not** share your `.env` file; use `.env.example` for sharing.

---

## 🙌 Author

Developed by **Nagapriyatham Pindi**  
Contact: [pindi.n@northeastern.edu](mailto:pindi.n@northeastern.edu)
