import streamlit as st
st.title("Quiz App")
test = st.text_input("What is the capital of France?")
if st.button("Submit"):
    if test.lower() == "paris":
        st.success("Correct!")
    else:
        st.error("Incorrect. The correct answer is Paris.")
        
