import streamlit as st
from dbweb.utils import run_query

def custom_sql():
    st.header("Custom SQL Query")
    sql = st.text_area("Enter SQL query:")
    if st.button("Run Query"):
        result = run_query(sql)
        if isinstance(result, list):
            st.dataframe(result)
        else:
            st.write(result)