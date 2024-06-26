-- 코드를 작성해주세요
select sum(score) as score, employ.emp_no, emp_name, position, email
from hr_grade as grade
join hr_employees as employ on grade.emp_no = employ.emp_no
join hr_department as dept on employ.dept_id = dept.dept_id
where year = 2022
group by emp_no
order by score desc
limit 1