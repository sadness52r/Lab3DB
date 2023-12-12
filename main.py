from config import *
import Psycopg2Test
import SQLiteTest
import PandasTest

print('Psycopg2 times:', Psycopg2Test.RunQueries())
print('SQLite times:', SQLiteTest.RunQueries())
print('Pandas times:', PandasTest.RunQueries())