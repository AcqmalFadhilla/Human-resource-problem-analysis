"""
Author: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
Date: 2024-12-01 23:42:42
LastEditors: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
LastEditTime: 2024-12-02 13:30:40
FilePath: utils.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
from pickle import load

class Convert:
    def __init__(self):
        pass
    
    def age(self, age):
        try:
            age = int(age)
            if 15 <= age <= 24:
                return 4 # Young age
            elif 25 <= age <= 34:
                return 0 # Early worker age
            elif 35 <= age <= 44:
                return 1 # Middle age
            elif 45 <= age <= 54:
                return 2 # Pre-retirement age
            elif age >= 55:
                return 3 # Retirement age
        except:
            raise ValueError("Invalid Age")
        
    def salary(self, salary):
        try:
            salary = int(salary)
            if salary <= 7500:
                return 1 # Low Salary
            elif salary <= 15000:
                return 2 # Medium Salary
            elif salary > 15000:
                return 3 # High Salary
        except:
            raise ValueError("Invalid Salary")
        
    def stay(self, stay):
        try:
            if stay == "short":
                return 2 # Short stay
            elif stay == "medium":
                return 1 # Medium stay
            elif stay == "long":
                return 0 # Long stay
        except:
            raise ValueError("Invalid Stay")
        
    def experience(self, experience):
        try:
            if experience == "Fresh Graduate":
                return 0 # Fresh Graduate
            elif experience == "Junior Employee":
                return 1 # Junior Employee
            elif experience == "Mid-level Employee":
                return 2 # Mid-level Employee
            elif experience == "Senior Employee":
                return 3 # Senior Employee
        except:
            raise ValueError("Invalid Epxrience")
        
    def gender(self, gender):
        try:
            if gender == "Male":
                return 1 # Male 
            elif gender == "Female":
                return 0 # Female
        except:
            raise ValueError("Invalid Gender")
        
    def department(self, department):
        try:
            if department == "Human Resource":
                return 0 # Human Resource
            elif department == "Research & Development":
                return 1 # Research & Development
            elif department == "Sales":
                return 2 # Sales
        except:
            raise ValueError("Invalid Department")
        
    def work_life_balance(self, work_life_balance):
        try:
            if work_life_balance == "Low":
                return 1 # Low
            elif work_life_balance == "Good":
                return 2 # Good
            elif work_life_balance == "Excellent":
                return 3 # Excellent
            elif work_life_balance == "Outstanding":
                return 4 # Outstandinf
        except:
            raise ValueError("Invalid Work Life Balance")
        
    def marital_status(self, marital_status):
        try:
            if marital_status == "Single":
                return 2 # Single
            elif marital_status == "Married":
                return 1 # Married
            elif marital_status == "Divorced":
                return 0 # Divorced
        except:
            raise ValueError("Invalid Marital Status")
        
    def over_time(self, over_time):
        try:
            if over_time == "Yes":
                return 1
            elif over_time == "No":
                return 0
        except:
            raise ValueError("Invalid Over Time")
        
class Preprocessing:
    def __init__(self):
        pass
    
    def preprocess(self, data):
        sc = load(open("models/scaler.pkl", "rb"))
        data_standard = sc.transform(data)
        return data_standard
    

        
        
        
        
        
