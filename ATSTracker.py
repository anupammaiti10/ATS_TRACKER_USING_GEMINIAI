import os
import google.generativeai as genai
import streamlit as st
import PyPDF2 as pdf
from dotenv import load_dotenv
load_dotenv()

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def gemini_output(input):
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(input)
    return response.text

# It is important to note that PyPDF2 may not always be able to extract text from PDFs that contain images or have non-standard structures. In such cases, you might need to use other libraries like PDFMiner or PyMuPDF for better results.Additionally, PyPDF2 is not an OCR (Optical Character Recognition) tool, so it cannot extract text from scanned PDFs. For such cases, you might need to use OCR software like Tesseract.
def extract_pdf_text(file):
    pdf_reader=pdf.PdfReader(file)
    text=""
    for page in pdf_reader.pages:
         text+=page.extract_text()
    return text


prompts="""Hey Act Like a skilled or very experience ATS(Application Tracking System)
with a deep understanding of tech field,software engineering,data science ,data analyst
and big data engineer. Your task is to evaluate the resume based on the given job description.
You must consider the job market is very competitive and you should provide 
best assistance for improving thr resumes. Assign the percentage Matching based 
on Jd and
the missing keywords with high accuracy
resume:{text}
description:{description}

I want the response in one single string having the structure
{{"JD Match":"%","MissingKeywords:[]","Profile Summary":""}}"""


# Streamlit UI Design 
st.title("ATS Tracker")
description=st.text_area("Enter your jod description here:", height=200)
Uploader=st.file_uploader("Upload your resume", type=["pdf"])
submit=st.button("Submit")
if submit:
   if description and Uploader:
       text=extract_pdf_text(Uploader)
       response=gemini_output(prompts)
       st.write(response,)

#This is not good projects because fo this ATS score that is not consider for any work purpose