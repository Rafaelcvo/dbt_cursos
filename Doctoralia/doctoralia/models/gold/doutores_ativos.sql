-- Modelo Gold: pronto para consumo em BI

select
    doctor_id,
    name,
    city1,
    telemedicine,
    'ativo' as status
from {{ ref('doutores_sp') }}
where telemedicine = 1
