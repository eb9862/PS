with heavy_users as (
    select host_id
    from PLACES
    group by host_id
    having count(name) >= 2
)

select place.id, place.name, place.host_id
from PLACES as place
join heavy_users as heavy
where place.host_id in (heavy.host_id)
order by place.id