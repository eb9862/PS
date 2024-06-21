-- 코드를 입력하세요
with
favorites_info as (
    select food_type, max(favorites) as max_favor
    from rest_info
    group by food_type
)

SELECT r.food_type, rest_id, rest_name, favorites
from rest_info as r
join favorites_info as favor
on r.food_type = favor.food_type
where favorites = favor.max_favor
order by 1 desc