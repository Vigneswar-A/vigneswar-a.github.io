SELECT TO_CHAR(sell_date,'yyyy-mm-dd') AS sell_date, 
    COUNT(product) AS num_sold, 
    LISTAGG(product,',') WITHIN GROUP ( ORDER BY product ASC) AS products
FROM (SELECT DISTINCT sell_date, product FROM Activities)A
GROUP BY sell_date