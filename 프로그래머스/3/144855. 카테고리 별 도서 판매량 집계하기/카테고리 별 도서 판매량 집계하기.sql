select book.category as CATEGORY,
    sum(sales) as TOTAL_SALES
from book as book
    right outer join book_sales as sales
    on book.book_id = sales.book_id
where year(sales.sales_date) = 2022 and
    month(sales.sales_date) = 1
group by book.category
order by book.category