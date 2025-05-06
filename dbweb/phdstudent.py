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
                query = "SELECT * FROM PhDStudent WHERE phdstudent_id = %s"
                result = run_query(query, (phdstudent_id,))
                if result:
                    st.write(result)
                else:
                    st.info("No PhDStudent found with that ID.")
            else:
                st.warning("Please enter a PhDStudent ID.")
    elif choice == "Add New PhDStudent":
        with st.form("add_phdstudent_form"):
            phdstudent_id = st.text_input("PhDStudent ID")
            name = st.text_input("Name")
            # Add more fields as needed based on schema
            submitted = st.form_submit_button("Add")
            if submitted:
                if phdstudent_id and name:
                    query = "INSERT INTO PhDStudent (phdstudent_id, name) VALUES (%s, %s)"
                    result = run_query(query, (phdstudent_id, name))
                    if result:
                        st.success("PhDStudent added successfully!")
                    else:
                        st.error("Failed to add PhDStudent.")
                else:
                    st.warning("Please fill in all required fields.")