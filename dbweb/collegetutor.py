import streamlit as st
from .utils import run_query

def collegetutor_management():
    st.header("CollegeTutor Management")

    # Search section
    with st.expander("Search College Tutors", expanded=True):
        search_id = st.text_input("Search by Tutor ID", "")
        if search_id:
            query = "SELECT tutor_id, name, CollegeFlatFloor FROM CollegeTutor WHERE tutor_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT tutor_id, name, CollegeFlatFloor FROM CollegeTutor"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No CollegeTutor records found.")

    # Add section
    st.subheader("Add New College Tutor")
    with st.form("add_collegetutor_form"):
        new_id = st.text_input("Tutor ID")
        new_name = st.text_input("Tutor Name")
        new_floor = st.text_input("College Flat Floor")
        submitted = st.form_submit_button("Add Tutor")
        if submitted:
            if not new_id or not new_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO CollegeTutor (tutor_id, name, CollegeFlatFloor) VALUES (%s, %s, %s)"
                result = run_query(insert_query, (new_id, new_name, new_floor))
                if result:
                    st.success(f"College Tutor '{new_name}' added successfully.")
                else:
                    st.error("Failed to add College Tutor. Check for duplicate ID or database error.")