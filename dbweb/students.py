import streamlit as st
from dbweb.utils import run_query

def student_management():
    st.header("Student Management")
    with st.expander("Search Students", expanded=True):
        col1, col2 = st.columns(2)
        with col1:
            search_id = st.text_input("Search by Student ID", "")
        with col2:
            search_name = st.text_input("Search by Name", "")
    query = "SELECT * FROM Student"
    params = []
    if search_id and search_name:
        query += " WHERE StudentID LIKE %s AND Name LIKE %s"
        params = [f"%{search_id}%", f"%{search_name}%"]
    elif search_id:
        query += " WHERE StudentID LIKE %s"
        params = [f"%{search_id}%"]
    elif search_name:
        query += " WHERE Name LIKE %s"
        params = [f"%{search_name}%"]
    students = run_query(query, params)
    if students:
        st.dataframe(students)
    else:
        st.info("No students found.")
    st.markdown("---")
    st.subheader("Add New Student")
    with st.form("add_student_form"):
        student_id = st.text_input("Student ID")
        name = st.text_input("Name")
        email = st.text_input("Email")
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
        major = st.text_input("Major Name")
        gpa = st.number_input("GPA", min_value=0.0, max_value=4.0, step=0.01)
        school = st.text_input("School Name")
        college = st.text_input("College Name")
        tuition = st.number_input("Tuition Fees", min_value=0.0, step=0.01)
        scholarships = st.text_input("Scholarships")
        financial_aids = st.text_input("Financial Aids")
        honors = st.text_input("Honors and Rewards")
        nation = st.text_input("Nation")
        phone = st.text_input("Phone Numbers")
        address = st.text_input("Mailing Address")
        emergency = st.text_input("Emergency Contact")
        grad_status = st.text_input("Graduate Status")
        submitted = st.form_submit_button("Add Student")
        if submitted:
            q = "INSERT INTO Student (StudentID, Name, Email, Gender, Year, MajorName, GPA, SchoolName, CollegeName, TuitionFees, Scholarships, FinancialAids, HonorsRewards, Nation, PhoneNumbers, MailingAddress, EmergencyContact, GraduateStatus) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
            params = (student_id, name, email, gender, year, major, gpa, school, college, tuition, scholarships, financial_aids, honors, nation, phone, address, emergency, grad_status)
            result = run_query(q, params)
            if result is not None:
                st.success("Student added successfully!")