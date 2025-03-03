'''
AI-Powered Resume GeneratorBuild a Streamlit app that takes user input (name, skills, experience, and education)
and generates a well-structured resume using the Gemini API. Format the output in markdown or PDF format.

API KEY = "AIzaSyDFbRTCN2WobGyv1dmXmTpXYm5LcKWWHBc"
'''

import streamlit as st 
import google.generativeai as genai
from fpdf import FPDF
import os

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
model = genai.GenerativeModel("gemini-2.0-flash")

name = st.text_input("Enter Your name ")
email = st.text_input("Enter your email id ")
skills = st.text_input("Enter Your skills in detail")
experience = st.text_input("Enter your experience")
education = st.text_input("Enter your education : marks : school/college name")

submit = st.button("Generate Resume")

if submit:
    response = model.generate_content(f'Write a profestional resume using only {name},{email},{skills},{experience},{education} . i want in nice format one below the other. i want no extra detail like what to improve just give me resume according to the information only And no bold text')
    resume_text = response.text
    st.write(resume_text)

    # Generate PDF using FPDF
    class PDF(FPDF):
        def header(self):
            self.set_font("Arial", "B", 16)
            self.cell(0, 10, f"Resume of {name}", ln=True, align="C")
            self.ln(10)

    pdf = PDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    for line in resume_text.split("\n"):
        pdf.multi_cell(0, 10, line)
        pdf.ln(1)

    pdf_path = "resume.pdf"
    pdf.output(pdf_path)

    # Provide a download button
    with open(pdf_path, "rb") as pdf_file:
        st.download_button(
            label="Download Resume as PDF",
            data=pdf_file,
            file_name=f"{name}_resume.pdf",
            mime="application/pdf",
        )

