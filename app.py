# app.py
# This is to create the UI that will provide a text area for users and display the results with visual feedback, using StreamLit.
import streamlit as st
from mood_analyzer import MoodAnalyzer
from ml_experiments import train_ml_model, predict_single_text
from dataset import SAMPLE_POSTS, TRUE_LABELS

# UI Config Setup
st.set_page_config(page_title="The Mood Machine: Rule vs. ML", page_icon="🤖")
st.title("🤖 The Mood Machina!")
st.markdown("Comparison of manual rules against machine learning logic.")

# Logic Initialization & Model Training
# Training should begin immediately once the app loads
@st.cache_resource # This ensures we only train the model once (one time), per session.
def initialize_models():
    rule_analyzer = MoodAnalyzer()
    #ML model learns patterns from the labeled datasets in SAMPLE_POSTS in dataset.py
    vectorizer, ml_model = train_ml_model(SAMPLE_POSTS, TRUE_LABELS)
    return rule_analyzer, vectorizer, ml_model

rule_analyzer, vectorizer, ml_model = initialize_models()

# Sidebar | Security & Dataset Context 
with st.sidebar:
    st.header("Training Data")
    st.info(f"This ML model is trained on {len(SAMPLE_POSTS)} labeled examples.")
    if st.checkbox("View Training Posts"):
        st.write(dict(zip(SAMPLE_POSTS, TRUE_LABELS)))

# Main UI
# Use success, error & info to give user immediate visual cues about the sentiment detected.
user_input = st.text_area("Enter a post to analyze:", placeholder="for example, 'Feeling tired but kind of hopeful'")

# Security Check: Prevent empty processing
if st.button("Analyze Mood Side-by-Side"):
    if not user_input.strip():
        st.warning("Please enter some text before analyzing.")
    else:
        # Execution: create two (2) columns for visual comparisons
        col1, col2 = st.columns(2)

        # --- Column 1: Rule-Based Results Analysis ---
        with col1:
            st.subheader("Rule-Based (Manual)")
            rb_label = rule_analyzer.predict_label(user_input)
            rb_explanation = rule_analyzer.explain(user_input)

            if rb_label == "positive": st.success(f"**Result: {rb_label.upper()}** 🎉")
            elif rb_label == "negative": st.error(f"**Result: {rb_label.upper()}** 😞")
            else: st.info(f"Result: {rb_label.upper()}")
            st.caption(f"Reasoning: {rb_explanation}")

        # --- Columnn 2: Machine Learning Results ---
        with col2:
            st.subheader("Machine Learning (Automated)")
            # This ML model will convert text to numbers and find the best matching label for it.
            ml_label = predict_single_text(user_input, vectorizer, ml_model)

            if ml_label == "positive": st.success(f"Result: {ml_label.upper()} 🎉")
            elif ml_label == "negative": st.error(f"Result: {ml_label.upper()} 😞")
            else: st.info(f"Result: {ml_label.upper()}")
            st.caption("Reasoning: Learned from training data patterns.")

st.markdown("---")
st.caption("Developed for CodePath AI110 - Section 1c | Mood Machine Lab")

# TO RUN, INSTALL STREAM OR ENSURED IT'S ALREADY INSTALLED 
# RUN pip install streamlit
# THEN RUN streamlit run app.py in the terminal to launch the app in your browser.

