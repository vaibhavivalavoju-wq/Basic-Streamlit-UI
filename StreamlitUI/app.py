import streamlit as st
from src.translator import translate_text

# Page Configuration
st.set_page_config(
    page_title="Language Translation Tool",
    page_icon="🌍",
    layout="centered"
)

# Title
st.title("🌍 Language Translation Tool")
st.write("Translate text between different languages.")

# Language Options
languages = {
    "English": "en",
    "Hindi": "hi",
    "Telugu": "te",
    "Tamil": "ta",
    "French": "fr",
    "Spanish": "es",
    "German": "de"
}

# Input Text
input_text = st.text_area(
    "Enter Text",
    height=150,
    placeholder="Type text to translate..."
)

# Language Selection
col1, col2 = st.columns(2)

with col1:
    source_lang = st.selectbox(
        "Source Language",
        list(languages.keys())
    )

with col2:
    target_lang = st.selectbox(
        "Target Language",
        list(languages.keys()),
        index=1
    )

# Translate Button
translate_btn = st.button(
    "🔄 Translate",
    use_container_width=True
)

# Output Section
if translate_btn:

    if input_text.strip() == "":
        st.warning("Please enter some text.")
    else:

        # Placeholder for translated text
        translated_text = translate_text(
            input_text, languages[source_lang], languages[target_lang])

        st.subheader("Translated Text")

        st.success(translated_text)

        # Optional Features
        col3, col4 = st.columns(2)

        with col3:
            st.button("📋 Copy")

        with col4:
            st.button("🔊 Speak")
