with longest as (
    select name.FISH_TYPE, name.FISH_NAME, max(info.LENGTH) as LENGTH
    from FISH_INFO as info
    join FISH_NAME_INFO as name
    on info.FISH_TYPE = name.FISH_TYPE
    group by info.FISH_TYPE, name.FISH_NAME
)

select info.ID, longest.FISH_NAME, longest.LENGTH
from longest
join FISH_INFO as info
on longest.FISH_TYPE = info.FISH_TYPE and longest.LENGTH = info.LENGTH
order by info.ID