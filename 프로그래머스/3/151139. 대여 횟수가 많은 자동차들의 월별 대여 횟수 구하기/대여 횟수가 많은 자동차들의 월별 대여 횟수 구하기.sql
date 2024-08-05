-- 코드를 입력하세요
with
btw_aug_oct as (
    select car_id
    from car_rental_company_rental_history
    where year(start_date) = 2022 and (month(start_date) >= 8 and month(start_date) <= 10)
    group by car_id
    having count(car_id) >= 5
),
id_for_needs as (
    select mon.car_id, rent.start_date
    from btw_aug_oct as mon
    join car_rental_company_rental_history as rent
    on rent.car_id = mon.car_id
)

SELECT month(start_date) as month, car_id, count(car_id) as records
from id_for_needs
where year(start_date) = 2022 and (month(start_date) >= 8 and month(start_date) <= 10)
group by month, car_id
order by month asc, car_id desc