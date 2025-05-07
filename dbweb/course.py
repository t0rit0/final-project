import streamlit as st
from .utils import run_query

def course_management():
    st.header("Course Management")

    # Search section
    with st.expander("Search Courses", expanded=True):
        search_id = st.text_input("Search by Course ID", "")
        if search_id:
            query = "SELECT course_id, name, career, credits, section, component, schedule, year, instructor_id, ta, grade_distribution, quota, location FROM Course WHERE course_id = %s"
            result = run_query(query, (search_id,))
        else:
            query = "SELECT course_id, name, career, credits, section, component, schedule, year, instructor_id, ta, grade_distribution, quota, location FROM Course"
            result = run_query(query)
        if result is not None:
            st.dataframe(result)
        else:
            st.info("No course records found.")

    # Add section
    st.subheader("Add New Course")
    with st.form("add_course_form"):
        new_id = st.text_input("Course ID")
        new_name = st.text_input("Course Name")
        new_career = st.text_input("Career")
        new_credits = st.number_input("Credits", min_value=0, step=1)
        new_section = st.text_input("Section")
        new_component = st.text_input("Component")
        new_schedule = st.text_input("Schedule")
        new_year = st.number_input("Year", min_value=1900, max_value=2100, step=1)
        new_instructor_id = st.text_input("Instructor ID")
        new_ta = st.text_input("TA")
        new_grade_distribution = st.text_area("Grade Distribution")
        new_quota = st.number_input("Quota", min_value=0, step=1)
        new_location = st.text_input("Location")
        submitted = st.form_submit_button("Add Course")
        if submitted:
            if not new_id or not new_name or not new_career or not new_credits or not new_section or not new_component or not new_schedule or not new_year or not new_instructor_id or not new_ta or not new_grade_distribution or not new_quota or not new_location:
                st.warning("Please fill in all fields.")
            else:
                insert_query = """INSERT INTO Course 
                    (course_id, name, career, credits, section, component, schedule, year, instructor_id, ta, grade_distribution, quota, location) 
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
                result = run_query(insert_query, (new_id, new_name, new_career, new_credits, new_section, new_component, new_schedule, new_year, new_instructor_id, new_ta, new_grade_distribution, new_quota, new_location))
                if result:
                    st.success(f"Course '{new_name}' added successfully.")
                else:
                    st.error("Failed to add course. Check for duplicate ID or database error.")