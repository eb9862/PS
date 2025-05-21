select
    concat(quarter(DIFFERENTIATION_DATE), 'Q') as QUARTER,
    count(ID) as ECOLI_COUNT
from ECOLI_DATA
group by concat(quarter(DIFFERENTIATION_DATE), 'Q')
order by concat(quarter(DIFFERENTIATION_DATE), 'Q')