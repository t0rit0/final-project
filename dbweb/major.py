import streamlit as st
from .utils import run_query

def major_management():
    st.header("Major Management")

    # Search section
    with st.expander("Search Majors", expanded=True):
        search_id = st.text_input("Search by Major ID", "")
        if search_id:
            query = "SELECT major_id, name, school_name, school_package, establishment_year FROM Major WHERE major_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT major_id, name, school_name, school_package, establishment_year FROM Major"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No major records found.")

    # Add section
    st.subheader("Add New Major")
    with st.form("add_major_form"):
        new_id = st.text_input("Major ID")
        new_name = st.text_input("Major Name")
        school_name = st.text_input("School Name")
        school_package = st.text_input("School Package")
        establishment_year = st.text_input("Establishment Year")
        submitted = st.form_submit_button("Add Major")
        if submitted:
            if not new_id or not new_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO Major (major_id, name, school_name, school_package, establishment_year) VALUES (%s, %s, %s, %s, %s)"
                result = run_query(insert_query, (new_id, new_name, school_name, school_package, establishment_year))
                if result:
                    st.success(f"Major '{new_name}' added successfully.")
                else:
                    st.error("Failed to add major. Check for duplicate ID or database error.")