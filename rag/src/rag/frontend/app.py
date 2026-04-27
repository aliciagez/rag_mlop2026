import streamlit as st
import httpx

API_URL = "http://localhost:8000"

def layout():
    st.markdown("#RAGnimals")
    st.markdown("ask me bout animals")

    text_input = st.text_input(label="ask a question")
    
    if st.button("Send") and text_input.strip() !="":
        response = httpx.post(f"{API_URL}/rag/query", json={"prompt": text_input}, timeout=120)

        data = response.json()

        st.markdown("## Question")
        st.markdown(text_input)
        
        st.markdown("## Answer")
        st.markdown(data.get("answer"))
        
        st.markdown("## Source")
        st.markdown(data.get("filename"))

if __name__ == "__main__":
    layout()
