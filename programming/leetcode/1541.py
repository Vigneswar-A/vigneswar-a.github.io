Select name, (case when travelled_distance is null then 0 else travelled_distance end) as travelled_distance from (SELECT NAME, SUM(DISTANCE) as travelled_distance FROM (USERS left JOIN RIDES ON USERS.ID = RIDES.USER_ID) GROUP BY users.id, name) 
order by travelled_distance desc, name
