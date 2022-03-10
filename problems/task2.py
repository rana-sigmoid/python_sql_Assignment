import psycopg2
import os
from sqlalchemy import create_engine
import pandas as pd
import config
import pandas.io.sql as sql
import pandasql as ps
import logging
import connectdb

# task2
# Write a python program to list the Total compensation  given till his/her last date or
# till now of all the employees till date in a xlsx file.
# columns required: Emp Name, Emp No, Dept Name, Total Compensation, Months Spent in Organization
class Task2:
    def task2(self,cursor):
        # update the end date to current date to find the month spent of each employee who are in the orgenisation
        update_end_date = "update jobhist set enddate=current_date where enddate is null"
        try:
            cursor.execute(update_end_date)  # this will execute the query
            logging.debug(f" updation executed on cursor - {cursor}")
        except:
            logging.error("failed to fetch ci=ursor from database")




        query = "SELECT  emp.ename, jh.empno, dept.dname, \
        round((jh.enddate - jh.startdate)/30) * jh.sal as total_compensation,\
        round((enddate - startdate)/30) as emp_month_spent \
        from jobhist as jh inner join emp on (jh.empno = emp.empno) inner join dept on (jh.deptno = dept.deptno);"
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

        path = "../Output/task2.xlsx"
        # adding data to excel file

        df.to_excel(path, header=False, index=False)



if __name__ == "__main__":
    obj = connectdb.connection_postgresql()
    cursor = obj.connect_db()
    obj_task=Task2()
    obj_task.task2(cursor)




