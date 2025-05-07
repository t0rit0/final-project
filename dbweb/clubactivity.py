import streamlit as st
from .utils import run_query

def club_activity_management():
    st.header("Club Activity Management")

    # Search section
    with st.expander("Search Club Activities", expanded=True):
        search_id = st.text_input("Search by Activity ID", "")
        if search_id:
            query = "SELECT * FROM ClubActivity WHERE activity_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT * FROM ClubActivity"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No club activity records found.")

    # Add section
    st.subheader("Add New Club Activity")
    with st.form("add_club_activity_form"):
        new_id = st.text_input("Activity ID")
        new_name = st.text_input("Activity Name")
        student_id = st.text_input("Student ID")
        club_name = st.text_input("Club Name")
        submitted = st.form_submit_button("Add Activity")
        if submitted:
            if not new_id or not new_name or not student_id or not club_name:
                st.warning("Please fill in all fields.")
            else:
                insert_query = "INSERT INTO ClubActivity (activity_id, name, student_id, club_name) VALUES (%s, %s, %s, %s)"
                result = run_query(insert_query, (new_id, new_name, student_id, club_name))
                if result:
                    st.success(f"Club Activity '{new_name}' added successfully.")
                else:
                    st.error("Failed to add club activity. Check for duplicate ID or database error.")