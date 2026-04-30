WITH payment_per_order AS (
    SELECT order_id, SUM(payment_value) AS total_payment
    FROM payments
    GROUP BY order_id
),

items_per_order AS (
    SELECT order_id, COUNT(*) AS item_count
    FROM items
    GROUP BY order_id
)

SELECT 
    pc.product_category_name_english AS category,
    SUM(p.total_payment * 1.0 / i.item_count) AS revenue
FROM payment_per_order p
JOIN items_per_order i ON p.order_id = i.order_id
JOIN items it ON p.order_id = it.order_id
JOIN products pr ON it.product_id = pr.product_id
JOIN products_category pc ON pr.product_category_name = pc.product_category_name
GROUP BY pc.product_category_name_english
ORDER BY revenue DESC;