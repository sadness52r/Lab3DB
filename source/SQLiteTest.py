from time import perf_counter
from config import *

queries = [
    """SELECT "VendorID", COUNT(*)
        FROM "TaxiDB" GROUP BY 1;""",
    """SELECT "passenger_count", AVG("total_amount")
       FROM "TaxiDB" GROUP BY 1;""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), COUNT(*)
       FROM "TaxiDB" GROUP BY 1, 2;""",
    """SELECT "passenger_count", STRFTIME('%Y', "tpep_pickup_datetime"), ROUND("trip_distance"), COUNT(*)
       FROM "TaxiDB" GROUP BY 1, 2, 3 ORDER BY 2, 4 DESC;""",
]

def RunQueries():
    averageTimes = []
    try:
        con = sq.connect(pathDB)
        cursor = con.cursor()
        for query in queries:
            totalTime = 0
            for _ in range (RUNS):
                start = perf_counter()
                cursor.execute(query)
                finish = perf_counter()
                totalTime += (finish - start)
            averageTimes.append(totalTime / RUNS)
    except Exception as _ex:
        print("[INFO] Error while working with TaxiDB.db (SQLite)", _ex)
    finally:
        cursor.close()
        if con:
            con.close()
        return averageTimes
