SELECT
  i.invoice_id,
  cu.customer_name,
  i.price,
  COUNT(c.contact_name) AS contacts_cnt,
  SUM(CASE WHEN c.contact_name IN (SELECT customer_name FROM customers) THEN 1 ELSE 0 END) AS trusted_contacts_cnt
FROM invoices i
LEFT JOIN contacts c ON i.user_id = c.user_id
LEFT JOIN customers cu ON i.user_id = cu.customer_id
GROUP BY i.invoice_id, i.price, cu.customer_name
ORDER BY i.invoice_id;