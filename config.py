from sqlalchemy import create_engine
import pathlib
from pathlib import Path
import psycopg2
import sqlite3 as sq
import pandas as pd

engine = create_engine('postgresql://postgres:euk721520022201@localhost:5432/TaxiDB')
#work_path = pathlib.Path.cwd()
#tiny = Path(work_path, 'DataBases', 'nyc_yellow_tiny.csv')
tinyDB = r'C:\pyProjects\Lab3DB\DataBases\TaxiDB.db'
tiny = r'C:\pyProjects\Lab3DB\DataBases\nyc_yellow_tiny.csv'
#big = 'nyc_yellow_big.csv'

dfTiny = pd.read_csv(tiny)
#dfBig = pd.read_csv(big)
#dfTiny["tpep_pickup_datetime"] = pd.to_datetime(dfTiny["tpep_pickup_datetime"])
#dfTiny.to_sql(db_name, engine, if_exists='replace', index=False)

RUNS = 10
host = "localhost"
user = "postgres"
password = "euk721520022201"
db_name = "TaxiDB"

# titles = {
# "Number": "INTEGER",
# "VendorID": "INTEGER",
# "tpep_pickup_datetime": "DATE",
# "tpep_dropoff_datetime": "DATE",
# "passenger_count": "REAL",
# "trip_distance": "REAL",
# "RatecodeID": "REAL",
# "store_and_fwd_flag": "TEXT",
# "PULocationID": "INTEGER",
# "DOLocationID": "INTEGER",
# "payment_type": "INTEGER",
# "fare_amount": "REAL",
# "extra": "REAL",
# "mta_tax": "REAL",
# "tip_amount": "REAL",
# "tolls_amount": "REAL",
# "improvement_surcharge": "REAL",
# "total_amount": "REAL",
# "congestion_surcharge": "REAL",
# "airport_fee": "REAL"
# }