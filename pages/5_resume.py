import streamlit as st
from streamlit_pdf_viewer import pdf_viewer

with open("assets/resume_Jennet_Zamanova.pdf", "rb") as file:
    st.download_button(
        label="Download resume as PDF",
        data = file,
        file_name="resume_Jennet_Zamanova.pdf",
        mime="text/plain",
    )

pdf_viewer(input="assets/resume_Jennet_Zamanova.pdf")
