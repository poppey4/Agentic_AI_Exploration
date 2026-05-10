import streamlit as st

st.title("AgentFlow AI")

st.subheader("Enterprise Multi-Agent AI Platform")

query = st.text_input("Ask a question")

if query:
    st.success(f"Processing Query: {query}")