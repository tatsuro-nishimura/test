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
    count(distinct b.lead_manager_code) num_lead_manager,
    count(distinct c.senior_manager_code) num_senior_manager,
    count(distinct d.manager_code) num_manager,
    count(distinct e.employee_code) num_employee
from
    (((company a
    left join
    lead_manager b
        on a.company_code = b.company_code)
    left join
    senior_manager c
        on b.lead_manager_code = c.lead_manager_code)
    left join
    manager d
        on c.senior_manager_code = d.senior_manager_code)
    left join
    employee e
        on d.manager_code = e.manager_code
group by company_code, founder
order by company_code
