"""
Author: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
Date: 2024-12-01 23:42:42
LastEditors: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
LastEditTime: 2024-12-02 07:15:38
FilePath: utils.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""

class Convert:
    def __init__(self):
        pass
    
    def age_group(self, age):
        try:
            age = int(age)
            if 15 <= age <= 24:
                return "Young Age"
            elif 25 <= age <= 34:
                return "Early worker age"
            elif 35 <= age <= 44:
                return "Middle Age"
            elif 45 <= age <= 54:
                return "Pre-retirement Age"
            elif age >= 55:
                return "Retirement Age"
            else:
                return "Other Age Group"
        except:
            return "Invalid Age"
        
    def salary_group(self, salary):
        try:
            salary = int(salary)
            if salary <= 7500:
                return "Low Salary"
            elif salary <= 15000:
                return "Medium Salary"
            else:
                return "High Salary"
        except:
            return "Invalid Salary"
        
    def stay_group(self, stay):
        try:
            stay = int(stay)
            if stay <= 5:
                return "Short"
            elif stay <= 10:
                return "Medium"
            else:
                return "Long"
        except:
            return "Invalid Stay"
        
    def experience_group(self, experience):
        try:
            experience = int(experience)
            if experience <= 1:
                return "Fresh Graduate"
            elif experience <= 3:
                return "Junior Employee"
            elif experience <= 5:
                return "Mid-level Employee"
            else:
                return "Senior Employee"
        except:
            return "Invalid Experience"
        
