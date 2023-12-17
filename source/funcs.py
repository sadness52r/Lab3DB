from config import *
import os
import sqlalchemy

def load_db():
    df1 = None
    df2 = None
    engine = create_engine(serverPath)
    if db_name not in sqlalchemy.inspect(engine).get_table_names():
        df2 = pd.read_csv(pathCSVTiny)
        df2["tpep_pickup_datetime"] = pd.to_datetime(df2["tpep_pickup_datetime"])
        df2["tpep_dropoff_datetime"] = pd.to_datetime(df2["tpep_dropoff_datetime"])
        df2.to_sql(db_name, engine, if_exists='replace', index=False, chunksize = 1000)
    engine.dispose()
    if not os.path.exists(pathDB):
        df1 = pd.read_csv(pathCSVBig)
        df1["tpep_pickup_datetime"] = pd.to_datetime(df1["tpep_pickup_datetime"])
        df1["tpep_dropoff_datetime"] = pd.to_datetime(df1["tpep_dropoff_datetime"])
        con = sq.connect(pathDB)
        df1.to_sql(db_name, con, if_exists='replace', index=False, chunksize=1000)
        con.close()