
  create or replace   view DBT_DEV_DB.analysis.hotel_count_by_day
  
   as (
    SELECT
  BOOKING_DATE,
  HOTEL,
  COUNT(ID) as count_bookings
FROM DBT_DEV_DB.transform.prepped_data
GROUP BY
  BOOKING_DATE,
  HOTEL
  );

