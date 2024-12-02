"""
Author: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
Date: 2024-12-01 18:36:30
LastEditors: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
LastEditTime: 2024-12-02 13:45:29
FilePath: app.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
import streamlit as st
import pandas as pd
from utils import Convert
from utils import Preprocessing
from pickle import load

# Intialise utils
convert = Convert()
preprocessing = Preprocessing()

# Initialise form
with st.form("predict"):
    st.title("Employee Leave Prediction")
    name = st.text_input("Name:",
                         placeholder="Input your name here")
    age = st.number_input("Age:", 
                          min_value=17,
                          max_value=75, 
                          placeholder="Input your age here")
    salary = st.number_input("Salary:",
                             placeholder="Input your salary here",
                             min_value=0)
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
                              ["Human Resource", "Research & Development", "Sales"])
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
        # Convert data
        data = {
            "Gender": convert.gender(gender),
            "AgeGroup": convert.age(age),
            "SalaryGroup": convert.salary(salary),
            "StayGroup": convert.stay(stay),
            "ExperienceGroup": convert.experience(work_experience),
            "Department": convert.department(department),
            "WorkLifeBalance": convert.work_life_balance(work_life_balance),
            "OverTime": convert.over_time(over_time),
            "MaritalStatus": convert.marital_status(marital_status),
            "YearsSinceLastPromotion": int(years_since_last_promotion),
        }
        
        # Convert to data frame
        df = pd.DataFrame([data])
        
        # Initialise preprocessing
        data_preprocessing = preprocessing.preprocess(df)
        
        # Model
        model = load(open("models/model_knn.pkl", "rb"))
        prediction = model.predict_proba(data_preprocessing)
        
        attritio_0 = prediction[0][0]
        attritio_1 = prediction[0][1]
        
        probability_0 = attritio_0 * 100
        probability_1 = attritio_1 * 100
        
        if attritio_0 > attritio_1:
            st.text(f'{probability_0:.2f} dan {probability_1:.2f}')
            st.warning(f"Employee which is name {name} has probability leave {probability_0:.2f}%")
        else:
            st.text(f'{probability_0:.2f} dan {probability_1:.2f}')
            st.success(f"Employee which is name {name} has probability stay {probability_1:.2f}%")

