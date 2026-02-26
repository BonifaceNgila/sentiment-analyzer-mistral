import streamlit as st
import requests
import os

st.title("Sentiment Analyzer (Mistral)")

backend_url = st.secrets.get("BACKEND_URL", os.getenv("BACKEND_URL", "http://localhost:8000")).rstrip("/")

text_input = st.text_area("Enter your sentence here:")

if st.button("Analyze"):
    try:
        response = requests.post(
            f"{backend_url}/analyze/",
            data={"text": text_input},
            timeout=60,
        )
        response.raise_for_status()
        sentiment = response.json().get("sentiment", "Error")
        st.subheader("Predicted Sentiment:")
        st.write(sentiment)
    except requests.RequestException as error:
        st.error(f"Could not reach backend API at {backend_url}. Error: {error}")