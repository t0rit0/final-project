import streamlit as st
from .utils import run_query

def collegetutor_management():
    st.header("CollegeTutor Management")

    # Search section
    with st.expander("Search College Tutors", expanded=True):
        search_id = st.text_input("Search by Tutor ID", "")
        if search_id:
            query = "SELECT StudentID, CollegeFlatFloor FROM CollegeTutor WHERE StudentID = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT StudentID, CollegeFlatFloor FROM CollegeTutor"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No CollegeTutor records found.")

    # Add section
    st.subheader("Add New College Tutor")
    with st.form("add_collegetutor_form"):
        new_id = st.text_input("Student ID")
        new_floor = st.text_input("College Flat Floor")
        submitted = st.form_submit_button("Add Tutor")
        if submitted:
            if not new_id:
                st.warning("Please fill in Student ID.")
            else:
                insert_query = "INSERT INTO CollegeTutor (StudentID, CollegeFlatFloor) VALUES (%s, %s)"
                result = run_query(insert_query, (new_id, new_floor))
                if result:
                    st.success("College Tutor added successfully.")
                else:
                    st.error("Failed to add College Tutor. Check for duplicate ID or database error.")