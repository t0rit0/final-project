import streamlit as st
from .utils import run_query

def course_management():
    st.header("Course Management")

    # Search section
    with st.expander("Search Courses", expanded=True):
        search_id = st.text_input("Search by Course ID", "")
        if search_id:
            query = "SELECT * FROM Course WHERE course_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT * FROM Course"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No course records found.")

    # Add section
    st.subheader("Add New Course")
    with st.form("add_course_form"):
        new_id = st.text_input("Course ID")
        new_name = st.text_input("Course Name")
        submitted = st.form_submit_button("Add Course")
        if submitted:
            if not new_id or not new_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO Course (course_id, name) VALUES (%s, %s)"
                result = run_query(insert_query, (new_id, new_name))
                if result:
                    st.success(f"Course '{new_name}' added successfully.")
                else:
                    st.error("Failed to add course. Check for duplicate ID or database error.")