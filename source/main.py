from config import *
import funcs
import Psycopg2Test
import SQLiteTest
import PandasTest
import SQLAlchemyTest
import DuckDBTest

funcs.load_db()
if Psycpog2: print('Psycopg2 times:', Psycopg2Test.RunQueries())
if SQLite3: print('SQLite3 times:', SQLiteTest.RunQueries())
if Pandas: print('Pandas times:', PandasTest.RunQueries())
if SQLAlchemy: print('SQLAlchemy times:', SQLAlchemyTest.RunQueries())
if DuckDB: print('DuckDB times:', DuckDBTest.RunQueries())
