import streamlit as st
from gtts import gTTS

st.title("🔊 Text to Voice")

text = st.text_area("Enter text:")

if st.button("Convert to Voice"):
    if text:
        tts = gTTS(text=text, lang="en")
        tts.save("output.mp3")

        st.audio("output.mp3", format="audio/mp3")
        st.success("Text converted to voice successfully!")
    else:
        st.warning("Please enter some text.")