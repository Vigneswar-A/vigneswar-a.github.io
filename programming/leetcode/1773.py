SELECT CONTEST_ID, round(COUNT(USER_ID)/(select count(*) from users)*100, 2) as percentage FROM REGISTER GROUP BY CONTEST_ID ORDER BY 2 desc, 1 asc
