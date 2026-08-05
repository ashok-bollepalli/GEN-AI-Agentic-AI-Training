import streamlit as st
import requests
import pandas as pd

# ============================
# FastAPI URL
# ============================
API_URL = "http://127.0.0.1:8000/api"

# ============================
# Page Config
# ============================
st.set_page_config(
    page_title="Student Management System",
    page_icon="🎓",
    layout="wide"
)

# ============================
# Header
# ============================
st.title("🎓 Student Management System")
st.write("### FastAPI + Streamlit REST API Demo")

# ============================
# Sidebar
# ============================
menu = st.sidebar.selectbox(
    "Select Operation",
    [
        "Create Student",
        "View Students",
        "Search Student"
    ]
)

# ======================================================
# CREATE STUDENT
# ======================================================
if menu == "Create Student":

    st.subheader("➕ Create Student")

    name = st.text_input("Student Name")

    course = st.selectbox(
        "Course",
        [
            "PYTHON",
            "JAVA",
            "DEVOPS",
            "GEN AI",
            "DATA SCIENCE"
        ]
    )

    fee = st.number_input(
        "Course Fee",
        min_value=1.0,
        step=100.0
    )

    if st.button("Save Student"):

        payload = {
            "name": name,
            "course": course,
            "fee": fee
        }

        response = requests.post(
            f"{API_URL}/student",
            json=payload
        )

        result = response.json()

        if response.status_code == 201:

            st.success(result.get("Message", "Student Created Successfully"))

            if "data" in result:

                df = pd.DataFrame([result["data"]])

                st.dataframe(
                    df,
                    use_container_width=True,
                    hide_index=True
                )

        else:
            st.error(result)

# ======================================================
# VIEW STUDENTS
# ======================================================
elif menu == "View Students":

    st.subheader("📋 Student List")

    if st.button("Load Students"):

        response = requests.get(f"{API_URL}/students")

        result = response.json()

        if response.status_code == 200:

            students = result["data"]

            df = pd.DataFrame(students)

            col1, col2, col3 = st.columns(3)

            col1.metric("Total Students", len(df))

            if "FEE" in df.columns:
                col2.metric("Total Fee", f"₹ {df['FEE'].sum():,.0f}")
                col3.metric("Average Fee", f"₹ {df['FEE'].mean():,.0f}")

            st.divider()

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.error(result.get("Message", "Unable to fetch students"))

# ======================================================
# SEARCH STUDENT
# ======================================================
elif menu == "Search Student":

    st.subheader("🔍 Search Student")

    student_id = st.number_input(
        "Student ID",
        min_value=1,
        step=1
    )

    if st.button("Search"):

        response = requests.get(
            f"{API_URL}/students/{student_id}"
        )

        result = response.json()

        if response.status_code == 200:

            student = result["data"]

            # Handle both object and list responses
            if isinstance(student, dict):
                df = pd.DataFrame([student])
            else:
                df = pd.DataFrame(student)

            st.success(result.get("Message", "Student Found"))

            st.dataframe(
                df,
                use_container_width=True,
                hide_index=True
            )

        else:
            st.error(result.get("Message", "Student Not Found"))