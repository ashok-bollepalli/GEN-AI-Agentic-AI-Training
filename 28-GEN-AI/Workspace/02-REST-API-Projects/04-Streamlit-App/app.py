import streamlit as st

st.title("Welcome to Streamlit")
st.write("This is my First Streamlit UI Application")

st.header("Course Details")
st.subheader("Streamlit UI")
st.write("Streamlit is used to create UI using Python.")
st.markdown("### This is markdown text")

name = st.text_input("Enter Student Name")
email = st.text_input("Enter Student Email")
course = st.selectbox(
    "Select Course",
    ["JAVA", "Python", "DevOps", "AI & ML"]
)
uploaded_file = st.file_uploader("Upload Your Resume :", type=["pdf", "docx"])

if st.button("Submit"):
    st.write("Given Name: ", name)
    st.write("Given Email: ", email)
    st.write("Selected Course: ", course)

if uploaded_file is not None:
    st.success("File uploaded successfully")
    st.write("File Name:", uploaded_file.name)