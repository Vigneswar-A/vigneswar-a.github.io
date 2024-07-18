SELECT  customer_id,COUNT(*) AS count_no_trans
	FROM Transactions t
	RIGHT JOIN Visits v ON v.visit_id = t.visit_id
	WHERE transaction_id is NULL
	GROUP BY customer_id