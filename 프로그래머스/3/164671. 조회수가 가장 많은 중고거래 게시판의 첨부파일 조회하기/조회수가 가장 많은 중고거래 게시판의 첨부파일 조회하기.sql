-- 코드를 입력하세요
with
board_file as (
    select board.views, board.board_id, file.file_id, file.file_name, file.file_ext
    from used_goods_board as board
    join used_goods_file as file
    on board.board_id = file.board_id
),
max_view as (
    select board_id, views
    from used_goods_board
    order by views desc
    limit 1
)

SELECT concat("/home/grep/src/", mx.board_id, "/", file_id, file_name, file_ext) as FILE_PATH
from board_file as bf
join max_view as mx on bf.board_id = mx.board_id
order by file_id desc