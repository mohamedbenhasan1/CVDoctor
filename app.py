import streamlit as st
from transformers import pipeline

corrector = pipeline("text2text-generation", model="prithivida/grammar_error_correcter_v1")

st.title("📄 CV Grammar Corrector")
st.markdown("Fix your résumé grammar using AI 🚀")

text = st.text_area("Paste your CV text here:")
if st.button("Correct My CV"):
    result = corrector(text)[0]['generated_text']
    st.success("✅ Corrected CV:")
    st.write(result)
