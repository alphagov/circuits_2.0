from google.cloud import bigquery
import pandas as pd

def save_to_bq(data):
    client = bigquery.Client(project='circuits-2point0')
    table_id = 'Circuits.workout_YYYYMMDD'

    job_config = bigquery.LoadJobConfig(
    schema=[
        bigquery.SchemaField("Exercise_name", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("Work", bigquery.enums.SqlTypeNames.STRING),
        bigquery.SchemaField("Rest", bigquery.enums.SqlTypeNames.STRING),
    ],
    write_disposition="WRITE_TRUNCATE",
    )
   
    job = client.load_table_from_dataframe(
    data, table_id, job_config=job_config
    )  # Make an API request.
    job.result()

    table = client.get_table(table_id)  # Make an API request.
    print(
        "Loaded {} rows and {} columns to {}".format(
        table.num_rows, len(table.schema), table_id
        )
    )
