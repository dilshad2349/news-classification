import streamlit as st
import joblib
model=joblib.load("news-classification-model.pkl")
news_labels={'0':'Technical','1':'business','2':'Sports','3':'Entertainment','4':'politics'}
st.title("News_classification")

user_input=st.text_area("enter your news here")

if st.button("predict"):
    predicted_label = model.predict([user_input])[0]
    predicted_news_label = news_labels[str(predicted_label)]
    st.info(f"predicted news label: {predicted_news_label}")

