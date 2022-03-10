import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd
import config
import pandas.io.sql as sql
import pandasql as ps
import logging
import connectdb


# Task 1
# Write a Python program to list employee numbers,names and their managers and save in a xlsx file.
# run_query("select * from dept")

class Task1:
    def task1(self, cursor):
        query = "select e1.empno,e1.ename as emp_name,e2.ename as mgr_name from emp as e1 INNER JOIN emp as e2 on (e1.mgr=e2.empno)"
        try:
            cursor.execute(query)  # this will execute the query
            logging.debug(f" query executed on cursor - {cursor}")
        except:
            logging.error("failed to fetch ci=ursor from database")

        # extracting all data from cursor
        query_result = cursor.fetchall()

        print(query_result)

        # inserting header in query result
        query_result.insert(0, [cursor.description[i].name for i in range(len(cursor.description))])

        # creating dataframe from data (list_type)
        df = pd.DataFrame(query_result)


        #path = "/Users/ranadilendrasingh/PycharmProjects/pythonsqlproject/Output/task1.xlsx"
        # adding data to excel file

        writer = pd.ExcelWriter('/Users/ranadilendrasingh/PycharmProjects/pythonsqlproject/Output/task1.xlsx')
        df.to_excel(writer, header=False, index=False)
        writer.save()
        #logging.info(f"Dataframe converted to excel stored in location -{path}")

if __name__ == "__main__":
    obj = connectdb.connection_postgresql()
    cursor = obj.connect_db()
    obj_task=Task1()
    obj_task.task1(cursor)
