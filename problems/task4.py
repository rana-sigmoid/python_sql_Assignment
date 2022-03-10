import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd
import config
import pandas.io.sql as sql
import pandasql as ps
import logging

class Task4:
    def task4(self):
        with pd.ExcelFile("../task2.xlsx") as xls:
            df = pd.read_excel(xls)

        data = df.groupby('dname').agg({"total_compensation": sum}).reset_index().rename(
            columns={"deptno": "Dept No", "dname": "Dept Name", "total_compensation": "Compensation"})
        data.to_excel("/Users/ranadilendrasingh/PycharmProjects/pythonsqlproject/Output/task4.xlsx", header=True, index=False)

        # print(data)

if __name__ == "__main__":

    obj_task=Task4()
    obj_task.task4()

