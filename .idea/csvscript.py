import os
import sys
import pandas as pd
from sqlalchemy import create_engine
import mysql.connector as msql
from mysql.connector import Error
import csv
x = range(1,10000)
x
covidData = pd.read_csv('https://raw.githubusercontent.com/mdcollab/covidclinicaldata/master/data/10-20_carbonhealth_and_braidhealth.csv', index_col=False)
#needs delimiter at end of each line so index_col=FALSE
covidData.head()
df = covidData.head()
conn_params_dic = {
    "host"      : "insert ip address",
    "database"  : "insert database",
    "user"      : "insert username",
    "password"  : "insert password"
}
def connect(conn_params_dic):
    conn = None
    try:
        print('Connecting to the MySQL...........')
        conn = msql.connect(**conn_params_dic)
        print("Connection successfully..................")

    except Error as err:
        print("Error while connecting to MySQL", err)
        # set the connection to 'None' in case of error
        conn = None
    return conn
def using_csv_reader(engine, datafrm, table_name):

    try:
        # Change your own path
        datafrm.to_csv('../CovidData/covid_bulk.csv', index=False)
        # dataframe columns with Comma-separated
        cols = ','.join(list(datafrm.columns))
        # SQL query to execute
        sql = "INSERT INTO %s(%s) VALUES(%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s,%%s)" % (table_name, cols)
        sql = sql.format(table_name)
        # Change your own path
        with open('../CovidData/covid_bulk.csv') as fh:
            reader = csv.reader(fh)
            next(reader)  # Skip firt line (headers)
            data = list(reader)
        engine.execute(sql, data)
        print("Data inserted using Using_csv_reader() successfully...")
    except Error as err:
        print("Error while inserting to MySQL", e)

conn = connect(conn_params_dic)
engine = using_alchemy()
using_csv_reader(engine, df, 'insert table name')