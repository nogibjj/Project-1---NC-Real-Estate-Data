import sqlite3
import pandas as pd
import dask.dataframe as dd
import os
import subprocess
import mysql.connector
from sqlalchemy import create_engine


# Create a database and table to store the real estate information
def createSQLitedb():
    connection = sqlite3.connect("datasets/data.db")
    stockPaths = pd.read_csv("datasets/stockPaths.csv", header=0)
    for eachStock in stockPaths.index:
        try:
            stockPath = stockPaths.loc[eachStock][0]
            stock = stockPath.split("/")[-1].split(".")[0]
            stockData = pd.read_csv(
                stockPath,
                header=0,
                parse_dates=["Date"],
                infer_datetime_format=True,
                dayfirst=True,
            )
            stockData.to_sql(
                f"{stock}_performance", connection, if_exists="replace", index=False
            )
            pass
        except:
            print(f"Error: {stock} not added to database")
            continue


def createdb(database, username, passwd, hostname, portnum):
    connection = mysql.connector.connect(
        user=username, password=passwd, host=hostname, port=portnum
    )
    cursor = connection.cursor()
    try:
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
    except mysql.connector.Error as err:
        print(f"Failed creating database: {err}")
        exit(1)
        pass
    connection.close()


# Create a table to store the real estate information
def updateTables(dbname, username, passwd, hostname, portnum):
    engine = create_engine(
        f"mysql://{username}:{passwd}@{hostname}:{portnum}/{dbname}")
    connection = engine.connect()
    realEstateData = pd.read_csv(
        'datasets/realtor-data.csv',
        header=0,
        parse_dates=["sold_date"],
        infer_datetime_format=True,
    )
    realEstateData.index = realEstateData.index.rename('index')
    realEstateData.to_sql(
        "real_estate", connection, if_exists="replace", index=False, chunksize=100_000
    )

# Pull the real estate data into a dataframe


def getData(dbname="realestate", username=os.getenv("AWS_REALESTATE_USERNAME"), passwd=os.getenv("AWS_REALESTATE_PASSWORD"), hostname=os.getenv("AWS_REALESTATE_HOSTNAME"), portnum=os.getenv("AWS_REALESTATE_PORT")):
    engine = create_engine(
        f"mysql://{username}:{passwd}@{hostname}:{portnum}/{dbname}")
    connection = engine.connect()
    realEstateData = pd.read_sql(
        'real_estate',
        connection
    )
    return realEstateData


# Send a query to the database
def query(query, database, username, passwd, hostname, portnum):
    connection = mysql.connector.connect(
        user=username, password=passwd, host=hostname, port=portnum
    )
    cursor = connection.cursor()
    cursor.execute(f"USE {database}")
    cursor.execute(query)
    for x in cursor:
        print(x)
    connection.close()
    pass

# Send a query to the database


def queryData(query, dbname="realestate", username=os.getenv("AWS_REALESTATE_USERNAME"), passwd=os.getenv("AWS_REALESTATE_PASSWORD"), hostname=os.getenv("AWS_REALESTATE_HOSTNAME"), portnum=os.getenv("AWS_REALESTATE_PORT")):
    engine = create_engine(
        f"mysql://{username}:{passwd}@{hostname}:{portnum}/{dbname}")
    connection = engine.connect()
    realEstateData = pd.read_sql(
        query,
        connection
    )
    return realEstateData


if __name__ == "__main__":
    myuser = os.getenv("AWS_REALESTATE_USERNAME")
    mypassword = os.getenv("AWS_REALESTATE_PASSWORD")
    myhost = os.getenv("AWS_REALESTATE_HOSTNAME")
    myport = os.getenv("AWS_REALESTATE_PORT")
    database = "realestate"
    # query("SELECT * FROM real_estate LIMIT 10", database, myuser, mypassword, myhost, myport)
    # getData(database, myuser, mypassword, myhost, myport)
    # createdb(database, myuser, mypassword, myhost, myport)
    # updateTables(database, myuser, mypassword, myhost, myport)
    # selectData(stock, database, myuser, mypassword, myhost, myport)
