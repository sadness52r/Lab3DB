from sqlalchemy import create_engine, text
import psycopg2
import sqlite3 as sq
import pandas as pd
import duckdb as dck
import pathlib
from pathlib import Path

# Flags to run and number of runs
RUNS = 20
Psycpog2 = False
SQLite3 = False
Pandas = False
SQLAlchemy = False
DuckDB = False

# Information to connect to PostgreSQL
host = ""  # name of host
port = ""  # number of port
user = ""  # name of user
password = ""  # password for PostgreSQL
db_name = ""  # name of database in PostgreSQL

# Information about data
name_table = "" 
nameDBFile = "" 
nameCSVBig = ""
nameCSVTiny = ""
folder_with_data = "" 

# Additional information
work_path = pathlib.Path.cwd()
pathCSVBig = Path(work_path, folder_with_data, nameCSVBig)
pathCSVTiny = Path(work_path, folder_with_data, nameCSVTiny)
pathDB = f"{folder_with_data}/{nameDBFile}"
serverPath = f"postgresql://{user}:{password}@{host}:{port}/{db_name}"
