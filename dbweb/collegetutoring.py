import streamlit as st
from dbweb.utils import run_query

def collegetutoring_management():
    st.header("CollegeTutoring Management")
    menu = ["Search by Student ID", "Add New CollegeTutoring"]
    choice = st.radio("Select Action", menu)
    if choice == "Search by Student ID":
        student_id = st.text_input("Enter Student ID")
        if st.button("Search"):
            if student_id:
                query = "SELECT * FROM CollegeTutoring WHERE StudentID = %s"
                result = run_query(query, (student_id,))
                if result:
                    st.write(result)
                else:
                    st.info("No CollegeTutoring found with that Student ID.")
            else:
                st.warning("Please enter a Student ID.")
    elif choice == "Add New CollegeTutoring":
        with st.form("add_collegetutoring_form"):
            student_id = st.text_input("Student ID")
            college_name = st.text_input("College Name")
            submitted = st.form_submit_button("Add")
            if submitted:
                if student_id and college_name:
                    query = "INSERT INTO CollegeTutoring (StudentID, CollegeName) VALUES (%s, %s)"
                    result = run_query(query, (student_id, college_name))
                    if result:
                        st.success("CollegeTutoring added successfully!")
                    else:
                        st.error("Failed to add CollegeTutoring.")
                else:
                    st.warning("Please fill in all required fields.")