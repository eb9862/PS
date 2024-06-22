-- 코드를 작성해주세요
with
emp_dep as (
    select emp.dept_id, emp.emp_name, dep.dept_name_en, sal
    from hr_employees as emp
    join hr_department as dep
    on emp.dept_id = dep.dept_id
)

select dept_id, dept_name_en, round(avg(sal)) as AVG_SAL
from emp_dep
group by dept_id
order by AVG_SAL desc