--some sql solutions
--chose Mysql

--https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
select name
from city
where
    countrycode = 'USA' and
    population > 120000

--https://www.hackerrank.com/challenges/japanese-cities-name/problem
select name
from city
where
    countrycode='JPN'


--https://www.hackerrank.com/challenges/the-company/problem
select
    a.company_code,
    a.founder,
    count(distinct b.lead_manager_code) as num_lead_manager,--'as ' can be omitted
    count(distinct c.senior_manager_code) as num_senior_manager,
    count(distinct d.manager_code) as num_manager,
    count(distinct e.employee_code) as num_employee
from
    (((company as a
    left join--this is equivalent to 'left outer join'
    lead_manager as b--'as ' can be omitted
        on a.company_code = b.company_code)
    left join
    senior_manager as c
        on b.lead_manager_code = c.lead_manager_code)
    left join
    manager as d
        on c.senior_manager_code = d.senior_manager_code)
    left join
    employee as e
        on d.manager_code = e.manager_code
group by company_code, founder
order by company_code
