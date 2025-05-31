import streamlit as st
from languageconvertor import translate

st.set_page_config(page_title = "EN to DE LLM Translator", page_icon = "🌍")

st.title("English -> German Translator DE")
st.markdown("Enter English text and get the translation.")

if "history" not in st.session_state:
    st.session_state.history = []

for role, msg in st.session_state.history:
    st.chat_message(role).markdown(msg)

prompt = st.chat_input("Type the English sentence...")
if prompt:
    st.session_state.history.append(("user", prompt))
    with st.chat_message("assistant"):
        with st.spinner("Getting the German translation..."):
            german = translate(prompt)
            st.write(german)
    st.session_state.history.append(("assistant", german))
