from langchain_helper import get_few_shot_db_chain
import streamlit as st 


st.title("Welcome😁 to JP-Rentals Search query the platform to find units🏠 in japan⛩️ based on your requirements.")

question = st.text_input("Question:  ")
if question:
    chain = get_few_shot_db_chain()
    answer = chain.invoke(question)
    st.header("Answer: ")
    st.write(answer)