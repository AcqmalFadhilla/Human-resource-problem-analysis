"""
Author: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
Date: 2024-12-01 18:36:30
LastEditors: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
LastEditTime: 2024-12-02 07:30:03
FilePath: app.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
import streamlit as st



# Initialise form
with st.form("predict"):
    name = st.text_input("Name:",
                         placeholder="Input your name here")
    age = st.number_input("Age:", 
                          min_value=17,
                          max_value=75, 
                          placeholder="Input your age here")
    salary = st.number_input("Salary:",
                             placeholder="Input your salary here")
    years_since_last_promotion = st.number_input("Years since last promotion:",
                                                 min_value=0,
                                                 max_value=20,
                                                 placeholder="Input your years since last promotion here")
    
    # Initialise columns
    col1, col2 = st.columns(2)
    with col1:
        gender = st.radio("Gender:",
                          ["Male", "Female"])
        
        stay = st.radio("How long do you stay:",
                        ["short", "medium", "long"],
                        captions=["you stay less than 5 years",
                                 "you stay between 5 and 10 years",
                                 "you stay more than 10 years"])
        work_life_balance = st.radio("Work life balance:",
                                     ["Low", "Good", "Excellent", "Outstanding"])

        marital_status = st.radio("Marital status:",
                                  ["Single", "Married", "Divorced"])
    
    with col2:
        department = st.radio("Department:",
                              ["Human Resource", "Resource & Development", "Sales"])
        work_experience = st.radio("Work experience:",
                                   ["Fresh Graduate", "Junior Employee", "Mid-level Employee", "Senior Employee"],
                                   captions=["your experience is less than 1 year",
                                             "your experience is between 1 and 3 years",
                                             "your experience is between 3 and 5 years",
                                             "your experience is more than 5 years"])
        
        over_time = st.radio("Over time:",
                             ["Yes", "No"])
        
    
    submit = st.form_submit_button("Predict")
    if submit:
        st.write(f"Name: {name}")
        st.write(f"Age: {age}")
        st.write(f"Salary: {salary}")
        st.write(f"Years since last promotion: {years_since_last_promotion}")
        st.write(f"How long do you stay?: {stay}")
        st.write(f"Work life balance: {work_life_balance}")
        st.write(f"Work experience: {work_experience}")
        st.write(f"Over time: {over_time}")




