import streamlit as st
from dbweb.utils import run_query

def enrolls_management():
    st.header("Enrolls Management")
    menu = ["Search by ID", "Add New Enrolls"]
    choice = st.radio("Select Action", menu)
    if choice == "Search by ID":
        enrolls_id = st.text_input("Enter Enrolls ID")
        if st.button("Search"):
            if enrolls_id:
                query = "SELECT * FROM Enrolls WHERE enrolls_id = %s"
                result = run_query(query, (enrolls_id,))
                if result:
                    st.write(result)
                else:
                    st.info("No Enrolls found with that ID.")
            else:
                st.warning("Please enter an Enrolls ID.")
    elif choice == "Add New Enrolls":
        with st.form("add_enrolls_form"):
            enrolls_id = st.text_input("Enrolls ID")
            student_id = st.text_input("Student ID")
            course_id = st.text_input("Course ID")
            grade = st.text_input("Grade")
            submitted = st.form_submit_button("Add")
            if submitted:
                if enrolls_id and student_id and course_id:
                    query = "INSERT INTO Enrolls (enrolls_id, student_id, course_id, grade) VALUES (%s, %s, %s, %s)"
                    result = run_query(query, (enrolls_id, student_id, course_id, grade))
                    if result:
                        st.success("Enrolls added successfully!")
                    else:
                        st.error("Failed to add Enrolls.")
                else:
                    st.warning("Please fill in all required fields.")