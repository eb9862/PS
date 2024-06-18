-- 코드를 입력하세요
with
car_history as (
    select car.car_id, car.car_type, history.start_date
    from car_rental_company_car as car
    join car_rental_company_rental_history as history
    on car.car_id = history.car_id
)

SELECT car_id
from car_history
where month(start_date) = 10 and car_type = "세단"
group by car_id
order by car_id desc