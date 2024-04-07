import os
import streamlit as st
import sqlite3

from langchain.llms import OpenAI
from langchain.sql_database import SQLDatabase
from langchain_experimental.sql import SQLDatabaseChain

# Set API keys
os.environ["OPENAI_API_KEY"] = "OpenAI key"

# Initialize OpenAI conversational AI model
from langchain_openai import OpenAI

# Main function
def main():
    st.title("TaskTalk")

    # Selection options on sidebar
    faculty_department = st.sidebar.selectbox("Select your department", ("AI", "Data Science"))

    # Load database based on department selection
    if faculty_department == "AI":
        db = SQLDatabase.from_uri("sqlite:///AI1.db")
    elif faculty_department == "Data Science":
        db = SQLDatabase.from_uri("sqlite:///DS1.db")

    # Chat on the right side
    with st.expander("Chat", expanded=True):
        messages = st.empty()
        if prompt := st.text_input("Say something"):
            db_chain = SQLDatabaseChain.from_llm(OpenAI(temperature=0), db, verbose=True)
            st.write("Assistant:", db_chain.run(prompt))

if __name__ == "__main__":
    main()
