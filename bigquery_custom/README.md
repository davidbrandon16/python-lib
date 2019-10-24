# Bigquery Custom

# requirement

|requirement| version|
| :---: | :---:|
| python| 3.7|
| bigquery| latest|


# Install

`pip install git+https://github.com/davidbrandon16/python-lib#subdirectory=bigquery_custom` 

## Create Object

```python
import bigquery_custom as bc
bq = bc.BigQuery("service.json")

```

## Execute Query

```python
import bigquery_custom as bc
bq = bc.BigQuery("service.json")
query = "SELECT * FROM product"
results =  bq.execute_query(query)
bq.bq_create_table()
```

## Create Table
```python
import bigquery_custom as bc
bq = bc.BigQuery("service.json")
columns = ["name","age"]
data_types = ["STRING", "INT64"]
mode = ["REQUIRED", "NULLABLE"]
table_ref = "project_id.package_name.table_name"
bq.bq_create_table(table_ref,columns, data_types, mode)
#if want to add partition just add partition name
```

## Insert Data Table
```python
import bigquery_custom as bc
bq = bc.BigQuery("service.json")
datas = ["David Brandon",23]
table_ref = "project_id.package_name.table_name"
bq.bq_insert_data(table_ref,datas)
```


## Delete Table
```python
import bigquery_custom as bc
bq = bc.BigQuery("service.json")
table_ref = "project_id.package_name.table_name"
bq.bq_delete_table(table_ref)
```