select data1.ID, count(data2.PARENT_ID) as CHILD_COUNT
from ECOLI_DATA as data1
left outer join ECOLI_DATA as data2
on data1.ID = data2.PARENT_ID
group by data1.ID