# 🛡️ SpamGuard — AI-Powered Spam Email Detector

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://spamguard-unh923mcv7n7qjaybmveuc.streamlit.app)

A machine learning web app that detects whether a message is **spam or not spam** using Natural Language Processing and a Random Forest classifier.

---

## 🚀 Live Demo

👉 [**Try SpamGuard Live**](https://spamguard-unh923mcv7n7qjaybmveuc.streamlit.app)

---

## 🧠 How It Works

1. **Text Preprocessing** — the input message goes through a full NLP pipeline:
   - Lowercasing
   - Punctuation removal
   - Tokenization
   - Stopword removal
   - Stemming (Porter Stemmer)

2. **Feature Extraction** — cleaned text is converted to numbers using **TF-IDF Vectorization**

3. **Classification** — a **Random Forest Classifier** predicts spam or not spam

---

## 📊 Model Performance

| Model | Accuracy | False Positives | False Negatives |
|---|---|---|---|
| Naive Bayes | 96.6% | 1 | 37 |
| **Random Forest** ✅ | **97.5%** | **0** | **28** |
| Logistic Regression | 95.6% | 1 | 48 |

Random Forest was chosen as the final model for its highest accuracy and zero false positives.

---

## 📁 Project Structure

```
SpamGuard/
├── app.py            ← Streamlit web app
├── main.ipynb        ← Model training notebook
├── model.pkl         ← Trained Random Forest model
├── vectorizer.pkl    ← Fitted TF-IDF vectorizer
├── spam.tsv          ← SMS Spam Collection dataset
└── requirements.txt  ← Python dependencies
```

---

## 🗂️ Dataset

**SMS Spam Collection Dataset**
- 5,572 real SMS messages labeled as spam or ham
- Source: [Justin Markham's PyConTutorial](https://github.com/justmarkham/pycon-2016-tutorial)

---

## 🛠️ Tech Stack

- **Python** — core language
- **Streamlit** — web app framework
- **scikit-learn** — ML model & TF-IDF vectorizer
- **NLTK** — NLP preprocessing
- **Pandas** — data manipulation
- **Pickle** — model serialization

---

## ⚙️ Run Locally

```bash
# Clone the repo
git clone https://github.com/aviksarkar0204-stack/SpamGuard.git
cd SpamGuard

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
```

---

## 🔮 Future Improvements

- [ ] Add user feedback (thumbs up/down) to collect new training data
- [ ] Retrain periodically with larger datasets
- [ ] Try SVM classifier for potentially higher accuracy
- [ ] Add bigram support in TF-IDF (`ngram_range=(1,2)`)

---

## 👨‍💻 Author

**Avik Sarkar**
- GitHub: [@aviksarkar0204-stack](https://github.com/aviksarkar0204-stack)

---

*This project was built as part of my ML learning journey. The model is trained on SMS data and is intended for educational/portfolio purposes.*
