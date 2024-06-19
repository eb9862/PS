-- 코드를 입력하세요
with
bd_usr as (
    select user_id, nickname, price, bd.status
    from used_goods_board as bd
    join used_goods_user as usr
    on bd.writer_id = usr.user_id
)

SELECT user_id, nickname, sum(price) as TOTAL_SALES
from bd_usr
where status = "DONE"
group by user_id
having TOTAL_SALES >= 700000
order by TOTAL_SALES