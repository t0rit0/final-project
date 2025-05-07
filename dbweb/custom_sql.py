import streamlit as st
from helper.sql_agent import get_sql_agent_advice, aget_sql_agent_advice
from dbweb.utils import run_query
import asyncio

def custom_sql():
    st.header("Custom SQL Advice & Warnings (Agent)")
    user_input = st.text_area("Describe your SQL task or question:")
    if st.button("Get SQL Advice"):
        if not user_input.strip():
            st.warning("Please enter a description or question.")
            return
        with st.spinner("Analyzing with SQL Agent..."):
            try:
                advice = asyncio.run(aget_sql_agent_advice(user_input))
            except RuntimeError:
                # If already in an event loop (e.g. Streamlit Cloud), fallback to create_task
                advice = asyncio.get_event_loop().run_until_complete(aget_sql_agent_advice(user_input))
        st.subheader("Agent Response:")
        st.json(advice)
    import sys
    import os
    sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'helper')))
    from helper.main import LLM
    
    st.header("Custom SQL Query")
    sql = st.text_area("Enter SQL query:")
    if st.button("Run Query"):
        result = run_query(sql)
        if isinstance(result, list):
            st.dataframe(result)
        else:
            st.write(result)
    pass
    
    # --- LLM Chatbox Sidebar ---
    if 'llm_chat_history' not in st.session_state:
        st.session_state['llm_chat_history'] = []
    if 'llm' not in st.session_state:
        st.session_state['llm'] = LLM()
    
    with st.sidebar:
        st.markdown("## 💬 LLM SQL Assistant")
        chat_input = st.text_input("Ask for SQL advice or generation:")
        if st.button("Send", key="llm_send") and chat_input:
            st.session_state['llm_chat_history'].append({"role": "user", "content": chat_input})
            async def get_llm_response():
                llm = st.session_state['llm']
                try:
                    response = await llm.openai_completion(chat_input, "You are a helpful SQL assistant. Generate or advise on SQL queries as requested.", [])
                    content = response['choices'][0]['message']['content']
                    st.session_state['llm_chat_history'].append({"role": "assistant", "content": content})
                except Exception as e:
                    st.session_state['llm_chat_history'].append({"role": "assistant", "content": f"Error: {e}"})
            asyncio.run(get_llm_response())
        for msg in st.session_state['llm_chat_history']:
            if msg['role'] == 'user':
                st.markdown(f"**You:** {msg['content']}")
            else:
                st.markdown(f"**LLM:** {msg['content']}")