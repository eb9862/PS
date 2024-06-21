-- 코드를 입력하세요
with
over_3 as (
    select writer_id, count(writer_id) as cnt
    from used_goods_board
    group by writer_id
    having cnt >= 3
)

SELECT user_id, nickname,
concat(city, " ", street_address1, " ", street_address2) as "전체주소",
concat(left(tlno, 3), "-", substr(tlno, 4, 4), "-", right(tlno, 4)) as "전화번호"
from used_goods_user as usr
inner join over_3
on usr.user_id = over_3.writer_id
order by user_id desc