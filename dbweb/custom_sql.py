import streamlit as st
from helper.sql_agent import get_sql_agent_advice
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
    
    # --- SQL Agent Sidebar ---
    if 'agent_chat_history' not in st.session_state:
        st.session_state['agent_chat_history'] = []
    
    with st.sidebar:
        st.markdown("## 💬 SQL Agent")
        agent_input = st.text_input("Ask for SQL advice:")
        if st.button("Get Advice", key="agent_send") and agent_input:
            st.session_state['agent_chat_history'].append({"role": "user", "content": agent_input})
            with st.spinner("Analyzing with SQL Agent..."):
                advice = get_sql_agent_advice(agent_input)
                st.session_state['agent_chat_history'].append({"role": "agent", "content": advice})
        for msg in st.session_state['agent_chat_history']:
            if msg['role'] == 'user':
                st.markdown(f"**You:** {msg['content']}")
            else:
                st.markdown(f"**Agent:**")
                st.json(msg['content'])