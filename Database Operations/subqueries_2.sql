select f_name,l_name,sal from  emp where sal>(select sal from emp where f_name="Sandesh");
select * from emp;
select f_name,l_name from emp where dept_id=(select dept_id from emp where dept_id=102);
select f_name,l_name from emp where  dept_id in (select dept_id from emp where l_name="Sandesh");
select f_name,l_name,sal from emp where sal>All(select avg(sal) from emp); 
select f_name,l_name,sal from emp where sal=(select min(sal) from emp); 
SELECT f_name,l_name, sal FROM emp WHERE dept_id IN (SELECT dept_id FROM emp WHERE job LIKE 'P%') AND sal > (SELECT avg(sal) FROM emp);
select f_name,l_name,sal from emp where sal >All(select sal from emp where f_name="Sarvesh");
