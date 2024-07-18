SELECT A.PLAYER_ID, TO_CHAR(A.EVENT_DATE, 'YYYY-MM-DD') EVENT_DATE, (SELECT SUM(GAMES_PLAYED) FROM ACTIVITY WHERE EVENT_DATE <= A.EVENT_DATE AND PLAYER_ID = A.PLAYER_ID) GAMES_PLAYED_SO_FAR FROM ACTIVITY A GROUP BY A.PLAYER_ID, A.EVENT_DATE