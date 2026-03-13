# app.py
# This is to create the UI that will provide a text area for users and display the results with visual feedback, using StreamLit.
import streamlit as st
from mood_analyzer import MoodAnalyzer
from dataset import SAMPLE_POSTS

# UI Config Setup
st.set_page_config(page_title="The Mood Machine", page_icon="🤖")
st.title("🤖 The Mood Machina")
st.markdown("---")

# Logic Initialization
analyzer = MoodAnalyzer()

# Sidebar | Security & Dataset Info
with st.sidebar:
    st.header("App Info")
    st.info("This app uses a Rule-Based model with negation handling logic.")
    if st.checkbox("Show Starter Posts"):
        st.write(SAMPLE_POSTS)

# Main UI
# Use success, error & info to give user immediate visual cues about the sentiment detected.
user_input = st.text_area("What's on your mind?", placeholder="Type a post here for example ('I am not chilling today')...")

# Security Check: Prevent empty processing
if st.button("Analyze Mood"):
    if not user_input.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        # Execution
        label = analyzer.predict_label(user_input)
        explanation = analyzer.explain(user_input)

        # UI Feedback Logic
        if label == "positive":
            st.success(f"**Result: {label.upper()}** 🎉")
        elif label == "negative":
            st.error(f"**Result: {label.upper()}** 😞")
        else: 
            st.info(f"**Reasoing:** {explanation}")

        st.write(f"**Reasoning:** {explanation}")

st.markdown("---")
st.caption("Developed for CodePath AI110 - Section 1c | Mood Machine Lab")

# TO RUN, INSTALL STREAM OR ENSURED IT'S ALREADY INSTALLED 
# RUN pip install streamlit
# THEN RUN streamlit run app.py in the terminal to launch the app in your browser.

