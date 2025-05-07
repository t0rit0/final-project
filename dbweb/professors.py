import streamlit as st
from dbweb.utils import run_query

def professor_management():
    st.header("Professor Management")
    with st.expander("Search Professors", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            search_id = st.text_input("Search by Instructor ID", "")
        with col2:
            search_name = st.text_input("Search by Name", "")
    query = "SELECT InstructorID, Name, Gender, Email, Title, SchoolName, Office, TeachingAssignments, Publications, Year, Salary, EducationBackground, ResearchField FROM Professor"
    params = []
    if search_id and search_name:
        query += " WHERE InstructorID LIKE %s AND Name LIKE %s"
        params = [f"%{search_id}%", f"%{search_name}%"]
    elif search_id:
        query += " WHERE InstructorID LIKE %s"
        params = [f"%{search_id}%"]
    elif search_name:
        query += " WHERE Name LIKE %s"
        params = [f"%{search_name}%"]
    professors = run_query(query, params)
    if professors:
        st.dataframe(professors)
    else:
        st.info("No professors found.")
    st.markdown("---")
    st.subheader("Add New Professor")
    with st.form("add_professor_form"):
        instructor_id = st.text_input("Instructor ID")
        name = st.text_input("Name")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        email = st.text_input("Email")
        title = st.text_input("Title")
        school = st.text_input("School Name")
        office = st.text_input("Office")
        teaching = st.text_area("Teaching Assignments")
        publications = st.text_area("Publications")
        year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
        salary = st.number_input("Salary", min_value=0.0, step=0.01)
        education = st.text_area("Education Background")
        research = st.text_input("Research Field")
        submitted = st.form_submit_button("Add Professor")
        if submitted:
            q = "INSERT INTO Professor (InstructorID, Name, Gender, Email, Title, SchoolName, Office, TeachingAssignments, Publications, Year, Salary, EducationBackground, ResearchField) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            params = (instructor_id, name, gender, email, title, school, office, teaching, publications, year, salary, education, research)
            result = run_query(q, params)
            if result is not None:
                st.success("Professor added successfully!")