import streamlit as st
from dbweb.utils import run_query

def collegetutoring_management():
    st.header("CollegeTutoring Management")
    menu = ["Search by ID", "Add New CollegeTutoring"]
    choice = st.radio("Select Action", menu)
    if choice == "Search by ID":
        collegetutoring_id = st.text_input("Enter CollegeTutoring ID")
        if st.button("Search"):
            if collegetutoring_id:
                query = "SELECT * FROM CollegeTutoring WHERE collegetutoring_id = %s"
                result = run_query(query, (collegetutoring_id,))
                if result:
                    st.write(result)
                else:
                    st.info("No CollegeTutoring found with that ID.")
            else:
                st.warning("Please enter a CollegeTutoring ID.")
    elif choice == "Add New CollegeTutoring":
        with st.form("add_collegetutoring_form"):
            collegetutoring_id = st.text_input("CollegeTutoring ID")
            tutor_id = st.text_input("Tutor ID")
            college_id = st.text_input("College ID")
            # Add more fields as needed based on schema
            submitted = st.form_submit_button("Add")
            if submitted:
                if collegetutoring_id and tutor_id and college_id:
                    query = "INSERT INTO CollegeTutoring (collegetutoring_id, tutor_id, college_id) VALUES (%s, %s, %s)"
                    result = run_query(query, (collegetutoring_id, tutor_id, college_id))
                    if result:
                        st.success("CollegeTutoring added successfully!")
                    else:
                        st.error("Failed to add CollegeTutoring.")
                else:
                    st.warning("Please fill in all required fields.")