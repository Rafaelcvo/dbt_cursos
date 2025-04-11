SELECT A.ID 
    , FIRST_NAME
    , LAST_NAME
    , birthdate
    , BOOKING_REFERENCE
    , HOTEL
    , BOOKING_DATE
    , COST
FROM DBT_DEV_DB.transform.customer  A
JOIN DBT_DEV_DB.transform.combined_bookings B
on A.ID = B.ID