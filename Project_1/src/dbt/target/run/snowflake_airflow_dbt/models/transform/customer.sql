
  create or replace   view DBT_DEV_DB.transform.customer
  
   as (
    SELECT ID 
    , FIRST_NAME
    , LAST_NAME
    , birthdate
FROM DBT_DEV_DB.JM.customers
  );

