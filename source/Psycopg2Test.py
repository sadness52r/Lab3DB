from time import perf_counter
from config import *

queries = [
    """SELECT "VendorID", COUNT(*)
        FROM "TaxiDB" GROUP BY 1;""",
    """SELECT "passenger_count", AVG("total_amount")
       FROM "TaxiDB" GROUP BY 1;""",
    """SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), COUNT(*)
       FROM "TaxiDB" GROUP BY 1, 2;""",
    """SELECT "passenger_count", EXTRACT(year FROM "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM "TaxiDB" GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
]

def RunQueries():
    averageTimes = []
    try:
        connection = psycopg2.connect(
            host = host,
            user = user,
            password = password,
            database = db_name
        )
        with connection.cursor() as cursor:
            for query in queries:
                totalTime = 0
                for _ in range (RUNS):
                    start = perf_counter()
                    cursor.execute(query)
                    finish = perf_counter()
                    totalTime += (finish - start)
                averageTimes.append(totalTime / RUNS)
    except Exception as _ex:
        print("[INFO] Error while working with PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
        return averageTimes
