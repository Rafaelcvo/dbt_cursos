with source as (
select 
    id,
    name,
    'I love dbt, snowflake and airflow' as description
from 
    DBT_DEV_DB.JM.tb_developer
)
select * from source