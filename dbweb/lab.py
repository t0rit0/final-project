import streamlit as st
from .utils import run_query

def lab_management():
    st.header("Lab Management")

    # Search section
    with st.expander("Search Labs", expanded=True):
        search_id = st.text_input("Search by Lab ID", "")
        if search_id:
            query = "SELECT * FROM Lab WHERE lab_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT * FROM Lab"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No lab records found.")

    # Add section
    st.subheader("Add New Lab")
    with st.form("add_lab_form"):
        new_id = st.text_input("Lab ID")
        new_name = st.text_input("Lab Name")
        submitted = st.form_submit_button("Add Lab")
        if submitted:
            if not new_id or not new_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO Lab (lab_id, name) VALUES (%s, %s)"
                result = run_query(insert_query, (new_id, new_name))
                if result:
                    st.success(f"Lab '{new_name}' added successfully.")
                else:
                    st.error("Failed to add lab. Check for duplicate ID or database error.")