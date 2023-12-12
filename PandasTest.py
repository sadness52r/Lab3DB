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
        for query in queries:
            totalTime = 0
            for _ in range (RUNS):
                start = perf_counter()
                pd.read_sql(query, con=engine)
                finish = perf_counter()
                totalTime += (finish - start)
            averageTimes.append(totalTime / RUNS)
    except Exception as _ex:
        print("[INFO] Error while working with Pandas", _ex)
    finally:
        engine.dispose()
        return averageTimes