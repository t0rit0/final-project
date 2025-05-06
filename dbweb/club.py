import streamlit as st
from .utils import run_query

def club_management():
    st.header("Club Management")

    # Search section
    with st.expander("Search Clubs", expanded=True):
        search_id = st.text_input("Search by Club ID", "")
        if search_id:
            query = "SELECT * FROM Club WHERE club_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT * FROM Club"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No Club records found.")

    # Add section
    st.subheader("Add New Club")
    with st.form("add_club_form"):
        new_id = st.text_input("Club ID")
        new_name = st.text_input("Club Name")
        submitted = st.form_submit_button("Add Club")
        if submitted:
            if not new_id or not new_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO Club (club_id, name) VALUES (%s, %s)"
                result = run_query(insert_query, (new_id, new_name))
                if result:
                    st.success(f"Club '{new_name}' added successfully.")
                else:
                    st.error("Failed to add Club. Check for duplicate ID or database error.")