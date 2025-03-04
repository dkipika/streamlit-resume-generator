'''
Sentiment Analysis of User Input
Create a Streamlit app where a user enters text, and the app analyzes its sentiment (positive, negative, or neutral).
Use Gemini API to classify the sentiment and display the result with a confidence score.
'''

import streamlit as st
import google.generativeai as genai
import os

api_key = st.secrets.get("GEMINI_API_KEY")
if not api_key:
    st.error("GEMINI_API_KEY not found. Please set it in Streamlit secrets.")
    st.stop()

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.0-flash")

st.header("Sentiment Analysis of User Input")
User_input = st.text_input("Enter Your Text")

if User_input:
    response = model.generate_content(f"Sentiment (positive, negative, or neutral) Analysis of User Input which is {User_input} and display the result with a confidence score")
    st.write(response.text)
