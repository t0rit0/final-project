import streamlit as st
from .utils import run_query

def college_management():
    st.header("College Management")

    # Search section
    with st.expander("Search Colleges", expanded=True):
        search_id = st.text_input("Search by College ID", "")
        if search_id:
            query = "SELECT * FROM College WHERE college_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT * FROM College"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No college records found.")

    # Add section
    st.subheader("Add New College")
    with st.form("add_college_form"):
        new_id = st.text_input("College ID")
        new_name = st.text_input("College Name")
        submitted = st.form_submit_button("Add College")
        if submitted:
            if not new_id or not new_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO College (college_id, name) VALUES (%s, %s)"
                result = run_query(insert_query, (new_id, new_name))
                if result:
                    st.success(f"College '{new_name}' added successfully.")
                else:
                    st.error("Failed to add college. Check for duplicate ID or database error.")