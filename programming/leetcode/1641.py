/* Write your PL/SQL query statement below */
SELECT name as country from ((SELECT duration, substr(phone_number, 0, 3) AS COUNTRY_CODE FROM (SELECT CALLER_ID AS ID, DURATION FROM CALLS UNION SELECT CALLEE_ID AS ID, DURATION FROM CALLS) NATURAL JOIN PERSON) natural join country) group by name having avg(duration) > (select avg(duration) from calls)


