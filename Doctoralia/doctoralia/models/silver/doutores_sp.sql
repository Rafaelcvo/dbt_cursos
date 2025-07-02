SELECT 
    doctor_id,
    title,
    name,
    city1,
    telemedicine
FROM  {{ ref('stg_doutores') }}
where name is not null
and city1 = 'São Paulo'