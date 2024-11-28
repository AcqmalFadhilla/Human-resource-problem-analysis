"""
Author: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
Date: 2024-11-28 19:24:11
LastEditors: Muhammad Acqmal Fadhilla Latief 109632348+AcqmalFadhilla@users.noreply.github.com
LastEditTime: 2024-11-28 21:29:29
FilePath: main.py
Description: 这是默认设置,可以在设置》工具》File Description中进行配置
"""
import os

import pandas as pd
from sqlalchemy import create_engine
from dotenv import  load_dotenv

# configure
load_dotenv()
DB_PASSWORD = os.environ.get("DB_PASSWORD")
URL = f"postgresql://postgres.pcsgtzzfvvpprapqehtl:{DB_PASSWORD}@aws-0-ap-southeast-1.pooler.supabase.com:6543/postgres"

engine = create_engine(URL)
df = pd.read_csv("data/df_exp.csv")
df.to_sql("data", engine)


