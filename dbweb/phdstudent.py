import streamlit as st
from dbweb.utils import run_query

def phdstudent_management():
    st.header("PhDStudent Management")
    menu = ["Search by ID", "Add New PhDStudent"]
    choice = st.radio("Select Action", menu)
    if choice == "Search by ID":
        student_id = st.text_input("Enter Student ID")
        if st.button("Search"):
            if student_id:
                query = "SELECT StudentID, Salary, TeachingAssistant, Supervisor, Lab, ResearchField, EducationBackground FROM PhDStudent WHERE StudentID = %s"
                result = run_query(query, (student_id,))
                if result:
                    st.dataframe(result)
                else:
                    st.info("No PhDStudent found with that ID.")
            else:
                st.warning("Please enter a PhDStudent ID.")
    elif choice == "Add New PhDStudent":
        with st.form("add_phdstudent_form"):
            student_id = st.text_input("Student ID")
            name = st.text_input("Name")
            salary = st.number_input("Salary", min_value=0)
            teaching_assistant = st.checkbox("Teaching Assistant")
            supervisor = st.text_input("Supervisor")
            lab = st.text_input("Lab")
            research_field = st.text_input("Research Field")
            education_background = st.text_area("Education Background")
            submitted = st.form_submit_button("Add")
            if submitted:
                if student_id and supervisor and lab and research_field:
                    query = "INSERT INTO PhDStudent (StudentID, Salary, TeachingAssistant, Supervisor, Lab, ResearchField, EducationBackground) VALUES (%s, %s, %s, %s, %s, %s, %s)"
                    result = run_query(query, (student_id, salary, teaching_assistant, supervisor, lab, research_field, education_background))
                    if result:
                        st.success("PhDStudent added successfully!")
                    else:
                        st.error("Failed to add PhDStudent.")
                else:
                    st.warning("Please fill in all required fields.")