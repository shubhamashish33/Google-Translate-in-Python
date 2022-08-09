import streamlit as st
from googletrans import Translator, LANGUAGES

output_text = ''


st.title('Google Translator with Python')


input_text = st.text_input('Enter the Source Text')

source_language = st.selectbox(
    'Select Source Language', list(LANGUAGES.values()))
Destination_language = st.selectbox(
    'Select Translated Language', list(LANGUAGES.values()))


if st.button('Translate'):
    trans = Translator()
    output = trans.translate(
        input_text, src=source_language, dest=Destination_language)
    output_text = output.text
    st.text(f"Translated Text would be: {output_text}")
