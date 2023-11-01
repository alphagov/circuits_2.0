from google.cloud import bigquery

from google.auth import default
import google.auth
credentials, project_id = google.auth.default()
creds, project_id = default()


def get_workout_type():
    client = bigquery.Client(project='circuits-2point0', credentials=creds)

    query = """
    SELECT *
    FROM `circuits-2point0.Circuits.Workout_types`
    """
    query_job = client.query(query)
    results = {}
    for w in query_job:
        results[w['New name']] = dict(w.items())
    return results


def get_exercises():
    client = bigquery.Client(project='circuits-2point0', credentials=creds)

    query = """
    SELECT *
    FROM `circuits-2point0.Circuits.Exercises`
    """

    query_job = client.query(query)
    results = []
    for row in query_job:
        results.append(dict(row.items()))

    return results
