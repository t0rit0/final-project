import streamlit as st
from .utils import run_query

def lab_management():
    st.header("Lab Management")

    # Search section
    with st.expander("Search Labs", expanded=True):
        search_id = st.text_input("Search by Lab ID", "")
        if search_id:
            query = "SELECT lab_id, name, InstructorID, StudentID, Funding, PhoneNumber, Email, Address, Fields, Subject FROM Lab WHERE lab_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT lab_id, name, InstructorID, StudentID, Funding, PhoneNumber, Email, Address, Fields, Subject FROM Lab"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No lab records found.")

    # Add section
    st.subheader("Add New Lab")
    with st.form("add_lab_form"):
        new_id = st.text_input("Lab ID")
        new_name = st.text_input("Lab Name")
        instructor_id = st.text_input("Instructor ID")
        student_id = st.text_input("Student ID")
        funding = st.number_input("Funding", min_value=0.0, step=0.01)
        phone = st.text_input("Phone Number")
        email = st.text_input("Email")
        address = st.text_area("Address")
        fields = st.text_input("Fields")
        subject = st.text_input("Subject")
        submitted = st.form_submit_button("Add Lab")
        if submitted:
            if not new_id or not new_name or not instructor_id or not student_id or not phone or not email or not address or not fields or not subject:
                st.warning("Please fill in all required fields.")
            else:
                insert_query = "INSERT INTO Lab (lab_id, name, InstructorID, StudentID, Funding, PhoneNumber, Email, Address, Fields, Subject) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                result = run_query(insert_query, (new_id, new_name, instructor_id, student_id, funding, phone, email, address, fields, subject))
                if result:
                    st.success(f"Lab '{new_name}' added successfully.")
                else:
                    st.error("Failed to add lab. Check for duplicate ID or database error.")