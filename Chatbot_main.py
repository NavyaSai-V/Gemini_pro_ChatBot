import os

import streamlit as st
from dotenv import load_dotenv
import numpy as np

import google.generativeai as gen_ai

load_dotenv()

with st.chat_message("user"):
    st.write("Hello ...")

with st.chat_message("assistant"):
    st.write("I am assistant")
    st.bar_chart(np.random.rand(30,3))

prompt = st.chat_input("say something")

if prompt:
    st.write(f"User has sent the following prompt: {prompt}")