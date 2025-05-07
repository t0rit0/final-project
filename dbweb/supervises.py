import streamlit as st
from dbweb.utils import run_query

def supervises_management():
    st.header("Supervises Management")
    menu = ["Search by ID", "Add New Supervises"]
    choice = st.radio("Select Action", menu)
    if choice == "Search by ID":
        supervises_id = st.text_input("Enter Supervises ID")
        if st.button("Search"):
            if supervises_id:
                query = "SELECT supervises_id, professor_id, phdstudent_id, lab_id FROM Supervises WHERE supervises_id = %s"
                result = run_query(query, (supervises_id,))
                if result:
                    st.dataframe(result)
                else:
                    st.info("No Supervises found with that ID.")
            else:
                st.warning("Please enter a Supervises ID.")
    elif choice == "Add New Supervises":
        with st.form("add_supervises_form"):
            supervises_id = st.text_input("Supervises ID")
            professor_id = st.text_input("Professor ID")
            phdstudent_id = st.text_input("PhDStudent ID")
            lab_id = st.text_input("Lab ID")
            submitted = st.form_submit_button("Add")
            if submitted:
                if supervises_id and professor_id and phdstudent_id and lab_id:
                    query = "INSERT INTO Supervises (supervises_id, professor_id, phdstudent_id, lab_id) VALUES (%s, %s, %s, %s)"
                    result = run_query(query, (supervises_id, professor_id, phdstudent_id, lab_id))
                    if result:
                        st.success("Supervises added successfully!")
                    else:
                        st.error("Failed to add Supervises.")
                else:
                    st.warning("Please fill in all required fields.")