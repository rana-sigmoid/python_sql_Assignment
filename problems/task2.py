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
# Write a python program to list the Total compensation  given till his/her last date or till now of all the employees till date in a xlsx file.
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

        query = "select emp.ename,emp.empno, dept.dname,sum(round((jh.enddate - jh.startdate)/30)*jh.sal) as total_compensation," \
                "date_part('month',age(jh.enddate, jh.startdate)) as emp_month_spent" \
                "from emp join dept on emp.deptno = dept.deptno join jobhist as jh on emp.empno = jh.empno GROUP BY emp.empno, dept.dname;"
        try:
            cursor.execute(query)  # this will execute the query
            logging.debug(f" query executed on cursor - {cursor}")
        except:
            logging.error("failed to fetch ci=ursor from database")
            # extracting all data from cursor
        query_result = cursor.fetchall()

        

        # inserting header in query result
        query_result.insert(0, [cursor.description[i].name for i in range(len(cursor.description))])

        # creating dataframe from data (list_type)
        df = pd.DataFrame(query_result)
        try:
            path = "/Users/ranadilendrasingh/PycharmProjects/pythonsqlproject/Output/task2.xlsx"
            # adding data to excel file
            df.to_excel(path, header=False, index=False)
            logging.info(f"Dataframe converted to excel stored in location -{path}")
        except:
            logging.error(f"Unable to convert dataframe to excel in location - {path}")


if __name__ == "__main__":
    obj = connectdb.connection_postgresql()
    cursor = obj.connect_db()
    obj_task=Task2()
    obj_task.task2(cursor)




