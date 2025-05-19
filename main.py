import os
import streamlit as st
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from dotenv import load_dotenv
from langchain.chat_models import ChatOpenAI
from newspaper import Article

# === Load API Key ===
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# === Configure Tesseract Manually ===
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# === Initialize LLM ===
llm = ChatOpenAI(model_name="gpt-4o", temperature=0.5, max_tokens=1000)

# === Streamlit UI ===
st.set_page_config(page_title="summaAIze", layout="centered")
st.title("📚 summaAIze")
st.sidebar.title("📤 Upload File or Paste URL")

uploaded_file = st.sidebar.file_uploader("Upload file (PDF, Image, or TXT)", type=["pdf", "png", "jpg", "jpeg", "txt"])
url_input = st.sidebar.text_input("or Paste URL (coming soon...)")

main_placeholder = st.empty()

# === Helper Functions ===
def extract_text_from_pdf(file):
    doc = fitz.open(stream=file.read(), filetype="pdf")
    return "\n".join([page.get_text() for page in doc])

def extract_text_from_image(file):
    image = Image.open(file)
    return pytesseract.image_to_string(image)

def summarize_and_analyze(text):
    prompt = f"""
    Given the following text, perform two tasks:
    1. Summarize the content in 5 bullet points.
    2. Analyze if the article shows any noticeable bias (positive, negative, or neutral).

    Text:
    {text}
    """
    return llm.predict(prompt)

def extract_text_from_url(url):
    article = Article(url)
    article.download()
    article.parse()
    return article.text

# === Main Execution ===
extracted_text = ""

if uploaded_file:
    filename = uploaded_file.name
    file_ext = filename.split(".")[-1].lower()
    st.info(f"📄 Processing {filename}...")

    try:
        if file_ext == "pdf":
            extracted_text = extract_text_from_pdf(uploaded_file)
        elif file_ext in ["png", "jpg", "jpeg"]:
            extracted_text = extract_text_from_image(uploaded_file)
        elif file_ext == "txt":
            extracted_text = uploaded_file.read().decode("utf-8")
        else:
            st.error("❌ Unsupported file type.")
    except Exception as e:
        st.error(f"❌ Error processing file: {e}")

elif url_input:
    st.info("🌐 Fetching article from URL...")
    try:
        extracted_text = extract_text_from_url(url_input)
        st.success("✅ Article fetched successfully!")
    except Exception as e:
        st.error(f"❌ Failed to fetch article: {e}")


else:
    st.info("👈 Upload a document or paste a URL to begin.")

# === Display Text + Summarization ===
if extracted_text:
    st.subheader("📜 Extracted Text Preview")
    st.text_area("Preview", extracted_text[:2000], height=200)

    st.download_button("⬇️ Download Extracted Text", extracted_text, file_name="extracted_text.txt")

    if st.button("🚀 Summarize and Detect Bias"):
        with st.spinner("Analyzing with GPT-4o..."):
            try:
                result = summarize_and_analyze(extracted_text)
                if "Bias:" in result:
                    summary_part, bias_part = result.split("Bias:", 1)
                    st.subheader("📝 Summary")
                    st.write(summary_part.strip())

                    st.subheader("🧠 Bias Detection")
                    st.write("Bias: " + bias_part.strip())
                else:
                    st.subheader("🔎 GPT Result")
                    st.write(result)
            except Exception as e:
                st.error(f"❌ LLM error: {e}")
