import streamlit as st
from .utils import run_query

def major_management():
    st.header("Major Management")

    # Search section
    with st.expander("Search Majors", expanded=True):
        search_name = st.text_input("Search by Major Name", "")
        if search_name:
            query = "SELECT MajorName, SchoolName, SchoolPackage, EstablishmentYear FROM Major WHERE MajorName = %s"
            result = run_query(query, (search_name,))
        else:
            query = "SELECT MajorName, SchoolName, SchoolPackage, EstablishmentYear FROM Major"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No major records found.")

    # Add section
    st.subheader("Add New Major")
    with st.form("add_major_form"):
        major_name = st.text_input("Major Name*")
        school_name = st.text_input("School Name*")
        school_package = st.text_input("School Package")
        establishment_year = st.number_input("Establishment Year", min_value=1800, max_value=2100)
        submitted = st.form_submit_button("Add Major")
        if submitted:
            if not major_name or not school_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO Major (MajorName, SchoolName, SchoolPackage, EstablishmentYear) VALUES (%s, %s, %s, %s)"
                result = run_query(insert_query, (major_name, school_name, school_package, establishment_year))
                if result:
                    st.success(f"Major '{major_name}' added successfully.")
                else:
                    st.error("Failed to add major. Check for duplicate ID or database error.")