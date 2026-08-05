import streamlit as st
import time

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------
st.set_page_config(
    page_title="Streamlit Widgets Demo",
    page_icon="🚀",
    layout="wide"
)

# ---------------------------------------------------
# Custom CSS
# ---------------------------------------------------
st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.main-title{
    text-align:center;
    color:#0F62FE;
    font-size:45px;
    font-weight:bold;
}

.sub-title{
    text-align:center;
    color:gray;
    font-size:20px;
    margin-bottom:25px;
}

.stButton>button{
    width:100%;
    background:#0F62FE;
    color:white;
    font-size:18px;
    border-radius:10px;
    height:50px;
}

.stButton>button:hover{
    background:#0043CE;
}

.box{
    padding:20px;
    border-radius:10px;
    background:white;
    box-shadow:0px 0px 10px rgba(0,0,0,0.1);
    margin-bottom:20px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.markdown("<h1 class='main-title'>🚀 Streamlit Widgets Demo</h1>", unsafe_allow_html=True)

st.markdown("<p class='sub-title'>Learn Streamlit Widgets with Beautiful UI</p>", unsafe_allow_html=True)

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

st.sidebar.title("📚 Menu")

option = st.sidebar.selectbox(
    "Choose Topic",
    ["Student Registration Demo"]
)

# ---------------------------------------------------
# Main UI
# ---------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("👨 Student Information")

    # text_input
    name = st.text_input("Enter Student Name")

    # selectbox
    course = st.selectbox(
        "Select Course",
        [
            "Python",
            "Java",
            "Data Science",
            "Gen AI",
            "DevOps"
        ]
    )

    st.markdown("</div>", unsafe_allow_html=True)

with col2:

    st.markdown("<div class='box'>", unsafe_allow_html=True)

    st.subheader("📝 Student Address")

    # text_area
    address = st.text_area(
        "Enter Address",
        height=120
    )

    # file uploader
    photo = st.file_uploader(
        "Upload Student Photo",
        type=["jpg","jpeg","png"]
    )

    st.markdown("</div>", unsafe_allow_html=True)

# ---------------------------------------------------
# Button
# ---------------------------------------------------

if st.button("💾 Save Student"):

    # Spinner
    with st.spinner("Saving student information..."):

        time.sleep(3)

    st.success("✅ Student Registered Successfully!")

    st.write("### Student Details")

    st.write("**Name :**", name)
    st.write("**Course :**", course)
    st.write("**Address :**", address)

    if photo:
        st.image(photo, width=200)

# ---------------------------------------------------
# Chat Input Demo
# ---------------------------------------------------

st.divider()

st.subheader("🤖 Chatbot Demo")

question = st.chat_input("Ask anything about Python...")

if question:

    st.write("👤 You:", question)

    with st.spinner("Thinking..."):

        time.sleep(2)

    st.success("🤖 AI Response")

    st.write(
        f"You asked **'{question}'**.\n\n"
        "This is a demo response generated using Streamlit Chat Input."
    )

# ---------------------------------------------------
# Footer
# ---------------------------------------------------

st.divider()

st.info("🎯 Streamlit Demo Application | Learn Streamlit Widgets Easily")