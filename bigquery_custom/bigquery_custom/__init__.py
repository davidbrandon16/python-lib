from google.cloud import bigquery
from google.oauth2 import service_account
import os

class BigQuery:

    def __init__(self,service_path=None):
        if service_path is not None :
            os.environ["GOOGLE_APPLICATION_CREDENTIALS"]=service_path

    def execute_query(self,query):
        client = bigquery.Client()
        query_job = client.query(query)
        return query_job.result()

    def bq_create_table(self,table_ref,columns=[], data_types=[], partition=None):
        if len(columns) ==0 or len(data_types) ==0:
            print("columns or data type must be filled")
            return
        if len(columns) != len(data_types):
            print("columns and data type must be same total array")
            return
        bigquery_client = bigquery.Client()
        # Prepares a reference to the table
        try:
            bigquery_client.get_table(table_ref)
        except Exception as e:
            schema = []
            for i in range(0,len(data_types)):
                schema.append(bigquery.SchemaField(columns[i], data_types[i], mode='REQUIRED'))
            table = bigquery.Table(table_ref, schema=schema)
            if partition is not None:
                table.time_partitioning = bigquery.TimePartitioning(type_=bigquery.TimePartitioningType.DAY,
                                                                field="process_time",
                                                                )
            table = bigquery_client.create_table(table)
            return_name = "Created table {}".format(table.table_id)
            if partition is not None:
                return_name = "{}, partitioned on column{}".format(return_name,table.time_partitioning)
            print(return_name)

    def bq_insert_data(self,datas,table_ref):
        bigquery_client = bigquery.Client()
        table = bigquery_client.get_table(table_ref)
        rows_to_insert = []
        for data in len(datas):
            if len(rows_to_insert)==5000:
                errors = bigquery_client.insert_rows(table, rows_to_insert)
                rows_to_insert = []
                print(errors)
            rows_to_insert.append(tuple(datas[data]))
            #print(rows_to_insert)
        assert errors == []


    def bq_delete_table(self,table_ref):
        bigquery_client = bigquery.Client()
        try:
            bigquery_client.get_table(table_ref)
            bigquery_client.delete_table(table_ref)
            print("success delete ", table_ref)
        except:
            return



