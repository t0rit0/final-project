import streamlit as st
from dbweb.utils import run_query

def phdstudent_management():
    st.header("PhDStudent Management")
    menu = ["Search by ID", "Add New PhDStudent"]
    choice = st.radio("Select Action", menu)
    if choice == "Search by ID":
        phdstudent_id = st.text_input("Enter PhDStudent ID")
        if st.button("Search"):
            if phdstudent_id:
                query = "SELECT phdstudent_id, name, salary, teaching_assistant, supervisor, lab, research_field, education_background FROM PhDStudent WHERE phdstudent_id = %s"
                result = run_query(query, (phdstudent_id,))
                if result:
                    st.dataframe(result)
                else:
                    st.info("No PhDStudent found with that ID.")
            else:
                st.warning("Please enter a PhDStudent ID.")
    elif choice == "Add New PhDStudent":
        with st.form("add_phdstudent_form"):
            phdstudent_id = st.text_input("PhDStudent ID")
            name = st.text_input("Name")
            salary = st.number_input("Salary", min_value=0)
            teaching_assistant = st.checkbox("Teaching Assistant")
            supervisor = st.text_input("Supervisor")
            lab = st.text_input("Lab")
            research_field = st.text_input("Research Field")
            education_background = st.text_area("Education Background")
            submitted = st.form_submit_button("Add")
            if submitted:
                if phdstudent_id and name and supervisor and lab and research_field:
                    query = "INSERT INTO PhDStudent (phdstudent_id, name, salary, teaching_assistant, supervisor, lab, research_field, education_background) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
                    result = run_query(query, (phdstudent_id, name, salary, teaching_assistant, supervisor, lab, research_field, education_background))
                    if result:
                        st.success("PhDStudent added successfully!")
                    else:
                        st.error("Failed to add PhDStudent.")
                else:
                    st.warning("Please fill in all required fields.")