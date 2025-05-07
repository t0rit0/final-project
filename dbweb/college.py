import streamlit as st
from .utils import run_query

def college_management():
    st.header("College Management")

    # Search section
    with st.expander("Search Colleges", expanded=True):
        search_name = st.text_input("Search by College Name", "")
        if search_name:
            query = "SELECT CollegeName, Description, Office, Budget, Location, Dean, EstablishmentYear, Warden FROM College WHERE CollegeName = %s"
            result = run_query(query, (search_name,))
        else:
            query = "SELECT CollegeName, Description, Office, Budget, Location, Dean, EstablishmentYear, Warden FROM College"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No college records found.")

    # Add section
    st.subheader("Add New College")
    with st.form("add_college_form"):
        new_name = st.text_input("College Name")
        new_description = st.text_area("Description")
        new_office = st.text_input("Office")
        new_budget = st.number_input("Budget", min_value=0.0, step=0.01)
        new_location = st.text_input("Location")
        new_dean = st.text_input("Dean")
        new_establishment_year = st.number_input("Establishment Year", min_value=1800, max_value=2100, step=1)
        new_warden = st.text_input("Warden")
        submitted = st.form_submit_button("Add College")
        if submitted:
            if not new_name or not new_description or not new_office or not new_budget or not new_location or not new_dean or not new_establishment_year or not new_warden:
                st.warning("Please fill in all fields.")
            else:
                insert_query = """INSERT INTO College 
                    (CollegeName, Description, Office, Budget, Location, Dean, EstablishmentYear, Warden) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
                result = run_query(insert_query, (new_name, new_description, new_office, new_budget, new_location, new_dean, new_establishment_year, new_warden))
                if result:
                    st.success(f"College '{new_name}' added successfully.")
                else:
                    st.error("Failed to add college. Check for duplicate ID or database error.")