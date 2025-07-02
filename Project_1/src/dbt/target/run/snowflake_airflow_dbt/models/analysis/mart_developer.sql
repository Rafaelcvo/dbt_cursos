
  create or replace   view DBT_DEV_DB.analysis.mart_developer
  
   as (
    with transform as (
select
    id,
    name,
    description,
    count(*) as qtd_developer
from 
    DBT_DEV_DB.transform.prepped_developer
group by
    id,name,description
)
select * from transform
  );

