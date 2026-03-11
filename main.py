import pickle
import re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("vectorizer.pkl", "rb") as f:
    vectorizer = pickle.load(f)

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

message = input("Enter your message: ")

# apply pipeline
message = to_lower(message)
message = remove_punctuation(message)
message = tokenize_message(message)
message = remove_stopwords(message)
message = stemming(message)
print("Preprocessed:", message)  # add this
message = " ".join(message)  # join back to string

message_transformed = vectorizer.transform([message])
prediction = model.predict(message_transformed)

if prediction[0] == 1:
    print("Spam")
else:
    print("Not spam")
