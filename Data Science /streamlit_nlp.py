import pandas as pd 
from sklearn.pipeline import Pipeline 
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import streamlit as st 

def load_model():
    df = pd.read_csv("youtube_comments.csv")
    model = Pipeline ([
    ('tfidf', TfidfVectorizer()),
    ('clf', LogisticRegression())
    ])
    model.fit(df['comment'], df['label'])
    return model 

model = load_model()

st.title("YT Comment Classifier")
st.write("Classify as Toxic or Supportive")

user_input = st.text_area("Enter a Youtube Comment")

if user_input:
    prediction = model.predict([user_input])[0]
    if prediction == "toxic":
        st.error("The comment is likely TOXIC")
    else:
        st.success("The comment is likely SUPPORTIVE")
    
