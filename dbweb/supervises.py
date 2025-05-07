import streamlit as st
from dbweb.utils import run_query

def supervises_management():
    st.header("Supervises Management")
    menu = ["Search by ID", "Add New Supervises"]
    choice = st.radio("Select Action", menu)
    if choice == "Search by ID":
        instructor_id = st.text_input("Enter Instructor ID")
        lab_id = st.text_input("Enter Lab ID")
        if st.button("Search"):
            if supervises_id:
                query = "SELECT InstructorID, LabID FROM Supervises WHERE InstructorID = %s AND LabID = %s"
                result = run_query(query, (instructor_id, lab_id))
                if result:
                    st.dataframe(result)
                else:
                    st.info("No Supervises found with that ID.")
            else:
                st.warning("Please enter a Supervises ID.")
    elif choice == "Add New Supervises":
        with st.form("add_supervises_form"):
            instructor_id = st.text_input("Instructor ID")
            lab_id = st.text_input("Lab ID")
            submitted = st.form_submit_button("Add")
            if submitted:
                if supervises_id and professor_id and phdstudent_id and lab_id:
                    query = "INSERT INTO Supervises (InstructorID, LabID) VALUES (%s, %s)"
                    result = run_query(query, (instructor_id, lab_id))
                    if result:
                        st.success("Supervises added successfully!")
                    else:
                        st.error("Failed to add Supervises.")
                else:
                    st.warning("Please fill in all required fields.")