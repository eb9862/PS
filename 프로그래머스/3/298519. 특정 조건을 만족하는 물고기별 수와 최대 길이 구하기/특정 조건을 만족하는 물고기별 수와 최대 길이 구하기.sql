# with info_not_null as (
#     select
#         ID,
#         FISH_TYPE,
#         ifnull(LENGTH, 10) as LENGTH,
#         TIME
#     from FISH_INFO
# )

select
    count(id) as FISH_COUNT,
    max(LENGTH) as MAX_LENGTH,
    FISH_TYPE
from FISH_INFO
group by FISH_TYPE
having avg(LENGTH) >= 33
order by FISH_TYPE