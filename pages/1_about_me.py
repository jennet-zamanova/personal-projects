import streamlit as st 

st.subheader("Jennet Zamanova")

# st.markdown("### [TrueTide](https://truetide-frontend.vercel.app/)")

# st.image("assets/Truetide.png", caption="TrueTide main page")

st.markdown(
    """
    I’m Jennet Zamanova, a computer science student at MIT with a passion for software engineering, machine learning, and data science. 
    I’ve interned at Vortexa Ltd, where I built scalable ETL pipelines using LLMs, and conducted research at MIT App Inventor to enhance debugging tools for developers. 
    As a lab assistant for MIT’s Machine Learning course (6.3900), I help students grasp complex concepts through hands-on support. 
    I’ve also led projects like Craftfolio, a crafts platform, and developed data-driven solutions for non-profits. 
    With experience in multiple programming languages and frameworks, I thrive on solving problems, building innovative systems, and collaborating with teams to make an impact.
"""
)

st.subheader("Find more about my projects!")

st.page_link("pages/2_class_projects.py", label="Class Projects", icon=":material/school:")
st.page_link("pages/3_urop_projects.py", label="Research Projects", icon=":material/devices:")
st.page_link("pages/4_club_projects.py", label="Club Projects", icon=":material/groups:")

st.subheader("And my experience!")
st.page_link("pages/5_resume.py", label="Resume", icon=":material/article:")
