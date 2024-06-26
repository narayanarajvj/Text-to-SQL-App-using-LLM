from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3

import google.generativeai as genai
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[1],question])
    return response.text

## Fucntion To retrieve query from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    cur.execute(sql)
    rows=cur.fetchall()
    conn.commit()
    conn.close()
    for row in rows:
        print(row)
    return rows

## Define Your Prompt
prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name STUDENT and has the following columns - NAME, CLASS, 
    SECTION and MARKS \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the students studying in Data Science class?, 
    the SQL command will be something like this SELECT * FROM STUDENT 
    where CLASS="Data Science"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """,
    """
    You are an expert in converting English questions to SQL queries.
    
    The SQL database is named EMPLOYEE and contains the following columns: NAME, LEVEL, 
    PRIMARY_SKILL, SECONDARY_SKILL, LOCATION and GENDER.
    
    **Examples:**
    
    Example 1: "How many entries of records are present?"
    SQL query: SELECT COUNT(*) FROM EMPLOYEE;
    
    Example 2: "Tell me all the employees skilled in Prompt."
    SQL query: SELECT * FROM EMPLOYEE WHERE PRIMARY_SKILL="Prompt" OR SECONDARY_SKILL="Prompt";
    
    Example 2: "Tell me all the employees highly skilled in Angular."
    SQL query: SELECT * FROM EMPLOYEE WHERE PRIMARY_SKILL="Angular";
    
    Example 3: "Tell me all the employee who are less proficient at prompt."
    SQL query: SELECT * FROM EMPLOYEE WHERE SECONDARY_SKILL="Prompt";
    
    **Instructions:**
    1. Convert each English question into a corresponding SQL query.
    2. Ensure the SQL query does not include backticks (```) in beginning or end and the word sql in the response.
    """
]

## Streamlit App

st.set_page_config(page_title="Text To SQL")
st.header("Gemini App To Retrieve SQL Data from Natural Text")

question=st.text_input("Input: ",key="input")

submit=st.button("Ask Query")

# if submit is clicked
if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    response=read_sql_query(response,"company1.db")
    st.subheader("The Response from Google Gemini Model is")
    for row in response:
        # print(row)
        st.header(row)