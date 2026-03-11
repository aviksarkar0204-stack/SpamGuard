import pickle
import re
import nltk
import streamlit as st
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('punkt_tab', quiet=True)

# ── Load model and vectorizer ─────────────────────────────────────────────────
@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
    with open("vectorizer.pkl", "rb") as f:
        vectorizer = pickle.load(f)
    return model, vectorizer

model, vectorizer = load_model()

# ── Preprocessing ─────────────────────────────────────────────────────────────
def to_lower(text):
    return text.lower()

def remove_punctuation(text):
    return re.sub(r'[^\w\s]', '', text)

def tokenize_message(text):
    return word_tokenize(text)

def remove_stopwords(text):
    stop_words = set(stopwords.words('english'))
    return [word for word in text if word not in stop_words]

def stemming(text):
    porter = PorterStemmer()
    return [porter.stem(word) for word in text]

def preprocess(message):
    message = to_lower(message)
    message = remove_punctuation(message)
    message = tokenize_message(message)
    message = remove_stopwords(message)
    message = stemming(message)
    return " ".join(message)

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="SpamGuard", page_icon="🛡️", layout="centered")

# ── Custom CSS ────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Syne:wght@400;600;800&display=swap');

html, body, [class*="css"] {
    font-family: 'Syne', sans-serif;
}

.stApp {
    background-color: #0a0a0f;
    background-image:
        radial-gradient(ellipse at 20% 20%, rgba(255, 60, 60, 0.08) 0%, transparent 50%),
        radial-gradient(ellipse at 80% 80%, rgba(60, 60, 255, 0.06) 0%, transparent 50%);
}

.header-wrapper {
    text-align: center;
    padding: 48px 0 32px 0;
}

.header-icon {
    font-size: 56px;
    display: block;
    margin-bottom: 12px;
    filter: drop-shadow(0 0 20px rgba(255, 80, 80, 0.5));
}

.header-title {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 42px;
    letter-spacing: -1px;
    color: #ffffff;
    margin: 0;
    line-height: 1;
}

.header-title span {
    color: #ff4444;
}

.header-sub {
    font-family: 'Space Mono', monospace;
    font-size: 13px;
    color: #555566;
    margin-top: 10px;
    letter-spacing: 2px;
    text-transform: uppercase;
}

.divider {
    border: none;
    border-top: 1px solid #1e1e2e;
    margin: 24px 0;
}

.stTextArea textarea {
    background-color: #111118 !important;
    border: 1px solid #2a2a3a !important;
    border-radius: 12px !important;
    color: #e0e0f0 !important;
    font-family: 'Space Mono', monospace !important;
    font-size: 14px !important;
    padding: 16px !important;
    transition: border-color 0.2s ease !important;
}

.stTextArea textarea:focus {
    border-color: #ff4444 !important;
    box-shadow: 0 0 0 2px rgba(255, 68, 68, 0.15) !important;
}

.stTextArea textarea::placeholder {
    color: #333344 !important;
}

.stTextArea label {
    font-family: 'Space Mono', monospace !important;
    font-size: 12px !important;
    color: #555566 !important;
    letter-spacing: 1.5px !important;
    text-transform: uppercase !important;
}

.stButton > button {
    background: linear-gradient(135deg, #ff4444 0%, #cc2222 100%) !important;
    color: white !important;
    border: none !important;
    border-radius: 10px !important;
    font-family: 'Syne', sans-serif !important;
    font-weight: 600 !important;
    font-size: 16px !important;
    padding: 14px 32px !important;
    letter-spacing: 0.5px !important;
    transition: all 0.2s ease !important;
    box-shadow: 0 4px 20px rgba(255, 68, 68, 0.25) !important;
}

.stButton > button:hover {
    transform: translateY(-2px) !important;
    box-shadow: 0 8px 28px rgba(255, 68, 68, 0.4) !important;
}

.result-spam {
    background: linear-gradient(135deg, #1a0505 0%, #2a0808 100%);
    border: 1px solid #ff4444;
    border-radius: 16px;
    padding: 32px;
    text-align: center;
    box-shadow: 0 0 40px rgba(255, 68, 68, 0.15), inset 0 1px 0 rgba(255,255,255,0.05);
    margin-top: 24px;
}

.result-safe {
    background: linear-gradient(135deg, #051a0a 0%, #082a10 100%);
    border: 1px solid #22cc55;
    border-radius: 16px;
    padding: 32px;
    text-align: center;
    box-shadow: 0 0 40px rgba(34, 204, 85, 0.12), inset 0 1px 0 rgba(255,255,255,0.05);
    margin-top: 24px;
}

.result-icon {
    font-size: 48px;
    display: block;
    margin-bottom: 12px;
}

.result-label-spam {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 32px;
    color: #ff4444;
    letter-spacing: -0.5px;
    margin: 0;
}

.result-label-safe {
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 32px;
    color: #22cc55;
    letter-spacing: -0.5px;
    margin: 0;
}

.result-desc {
    font-family: 'Space Mono', monospace;
    font-size: 12px;
    color: #555566;
    margin-top: 8px;
    letter-spacing: 1px;
    text-transform: uppercase;
}

.footer {
    text-align: center;
    font-family: 'Space Mono', monospace;
    font-size: 11px;
    color: #2a2a3a;
    margin-top: 48px;
    letter-spacing: 1px;
}

#MainMenu, footer, header {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-wrapper">
    <span class="header-icon">🛡️</span>
    <h1 class="header-title">SPAM<span>GUARD</span></h1>
    <p class="header-sub">AI-Powered Email Classifier · Random Forest Model</p>
</div>
<hr class="divider">
""", unsafe_allow_html=True)

# ── Input ─────────────────────────────────────────────────────────────────────
message = st.text_area(
    "MESSAGE INPUT",
    placeholder="Paste your email or message here...",
    height=180
)

st.markdown("<br>", unsafe_allow_html=True)
clicked = st.button("🔍  ANALYZE MESSAGE", use_container_width=True)

# ── Prediction ────────────────────────────────────────────────────────────────
if clicked:
    if not message.strip():
        st.warning("⚠️ Please enter a message to analyze.")
    else:
        with st.spinner("Analyzing..."):
            processed = preprocess(message)
            prediction = model.predict(vectorizer.transform([processed]))

        if prediction[0] == 1:
            st.markdown("""
            <div class="result-spam">
                <span class="result-icon">🚨</span>
                <p class="result-label-spam">SPAM DETECTED</p>
                <p class="result-desc">This message shows signs of spam or phishing</p>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown("""
            <div class="result-safe">
                <span class="result-icon">✅</span>
                <p class="result-label-safe">LOOKS SAFE</p>
                <p class="result-desc">No spam signals detected in this message</p>
            </div>
            """, unsafe_allow_html=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="footer">
    SPAMGUARD · BUILT WITH STREAMLIT · RANDOM FOREST CLASSIFIER
</div>
""", unsafe_allow_html=True)