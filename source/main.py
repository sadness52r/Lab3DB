from config import *
import os
import funcs
import Psycopg2Test
import SQLiteTest
import PandasTest
import SQLAlchemyTest
import DuckDBTest

funcs.load_db()
print('Psycopg2 times:', Psycopg2Test.RunQueries())
print('SQLite times:', SQLiteTest.RunQueries())
print('Pandas times:', PandasTest.RunQueries())
print('SQLAlchemy times:', SQLAlchemyTest.RunQueries())
print('DuckDB times:', DuckDBTest.RunQueries())