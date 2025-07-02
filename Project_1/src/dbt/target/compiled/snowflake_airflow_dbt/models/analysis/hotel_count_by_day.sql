SELECT
  BOOKING_DATE,
  HOTEL,
  COUNT(ID) as count_bookings
FROM DBT_DEV_DB.transform.prepped_data
GROUP BY
  BOOKING_DATE,
  HOTEL