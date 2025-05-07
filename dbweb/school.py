import streamlit as st
from .utils import run_query

def school_management():
    st.header("School Management")

    # Search section
    with st.expander("Search Schools", expanded=True):
        search_name = st.text_input("Search by School Name", "")
        if search_name:
            query = "SELECT * FROM School WHERE SchoolName LIKE %s"
            result = run_query(query, (f"%{search_name}%",))
        else:
            query = "SELECT * FROM School"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No school records found.")

    # Add section
    st.subheader("Add New School")
    with st.form("add_school_form"):
        col1, col2 = st.columns(2)
        with col1:
            school_name = st.text_input("School Name*")
            location = st.text_input("Location")
            website = st.text_input("Website")
            dean = st.text_input("Dean")
        with col2:
            establishment_year = st.number_input("Establishment Year", min_value=1800, max_value=2100)
            avg_gpa = st.number_input("Average GPA", min_value=0.0, max_value=4.0, step=0.01)
            scholarships = st.text_area("Scholarships")
        
        submitted = st.form_submit_button("Add School")
        if submitted:
            if not school_name:
                st.warning("Please fill in required fields (marked with *).")
            else:
                insert_query = """
                INSERT INTO School 
                (SchoolName, Location, Website, Dean, EstablishmentYear, SchoolAvgGPA, Scholarships)
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                result = run_query(insert_query, (
                    school_name, location, website, dean, 
                    establishment_year, avg_gpa, scholarships
                ))
                if result:
                    st.success(f"School '{school_name}' added successfully.")
                else:
                    st.error("Failed to add school. Check for duplicate name or database error.")