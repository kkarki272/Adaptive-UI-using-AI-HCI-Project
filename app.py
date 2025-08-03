import streamlit as st
from utils_module import analyze_sentiment


st.set_page_config(page_title="Adaptive Sentiment UI", layout="wide")

# App title
st.title("🎭 Adaptive User Interface with AI")
st.write("App Loaded Successfully")


# Input text
user_input = st.text_area("Type something (e.g., how are you feeling today?):")

if user_input:
    sentiment, score = analyze_sentiment(user_input)

    st.markdown(f"**Sentiment:** `{sentiment}` | **Confidence Score:** `{score:.2f}`")

    # UI adaptation based on sentiment
    if sentiment == "positive":
        st.balloons()
        st.success("You seem to be in a good mood! Enjoy the light-themed interface 🌞")
        st.markdown('<style>body {background-color: #f5f5f5; color: #000;}</style>', unsafe_allow_html=True)

    elif sentiment == "negative":
        st.error("Looks like you're feeling down. Switching to a calm, dark theme 🌙")
        st.markdown('<style>body {background-color: #2c2c2c; color: #fff;}</style>', unsafe_allow_html=True)

    else:
        st.info("Neutral tone detected. The interface remains unchanged.")

