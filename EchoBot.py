import os

import streamlit as st
from dotenv import load_dotenv
import numpy as np

import google.generativeai as gen_ai

load_dotenv()

st.title("Echo Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# prompt = st.chat_input("say something")

if prompt:= st.chat_input("say something"):

    st.chat_message("user").markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

response = f"Echo: {prompt}"

with st.chat_message("assistant"):
    st.markdown(response)

st.session_state.messages.append({"role": "assistant", "content": response})