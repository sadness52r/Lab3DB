from sqlalchemy import create_engine, text
import pathlib
from pathlib import Path
import psycopg2
import sqlite3 as sq
import pandas as pd
import duckdb as dck

RUNS = 20
host = "localhost"
port = '5432'
user = "postgres"
password = "euk721520022201"
db_name = "TaxiDB"
nameDBFile = 'TaxiDB.db'
nameCSVBig = 'nyc_yellow_big.csv'
nameCSVTiny = 'nyc_yellow_tiny.csv'
work_path = pathlib.Path.cwd()
pathCSVBig = Path(work_path, 'DataBases', nameCSVBig)
pathCSVTiny = Path(work_path, 'DataBases', nameCSVTiny)
pathDB = f'C:\pyProjects\Lab3DB\DataBases\{nameDBFile}'
serverPath = f'postgresql://{user}:{password}@{host}:{port}/{db_name}'