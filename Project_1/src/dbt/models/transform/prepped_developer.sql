with source as (
select 
    id,
    name,
    'I love dbt, snowflake and airflow' as description
from 
    {{ ref('tb_developer') }}
)
select * from source