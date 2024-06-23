-- 코드를 입력하세요
with
rent as (
    SELECT car_id,
    case
    when start_date <= "2022-10-16" and "2022-10-16" <= end_date
    then "대여중"
    end as AVAILABILITY
    from car_rental_company_rental_history
    order by car_id
),
rent2 as (
    select *
    from rent
    where availability is not null
)

select rental.car_id,
case
    when availability is null then "대여 가능"
    else availability
    end as availability
from car_rental_company_rental_history as rental
left join rent2 as rt
on rental.car_id = rt.car_id
group by rental.car_id
order by 1 desc