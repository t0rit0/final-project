import streamlit as st
from .utils import run_query

def school_management():
    st.header("School Management")

    # Search section
    with st.expander("Search Schools", expanded=True):
        search_id = st.text_input("Search by School ID", "")
        if search_id:
            query = "SELECT * FROM School WHERE school_id = %s"
            result = run_query(query, (search_id,))
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
        new_id = st.text_input("School ID")
        new_name = st.text_input("School Name")
        submitted = st.form_submit_button("Add School")
        if submitted:
            if not new_id or not new_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO School (school_id, name) VALUES (%s, %s)"
                result = run_query(insert_query, (new_id, new_name))
                if result:
                    st.success(f"School '{new_name}' added successfully.")
                else:
                    st.error("Failed to add school. Check for duplicate ID or database error.")