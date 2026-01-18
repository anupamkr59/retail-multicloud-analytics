-- Curated tables (logical representation)
-- curated_orders   -> data/curated/orders/curated_orders.csv
-- curated_payments -> data/curated/payments/curated_payments.csv

-- 1. Total orders and total revenue
SELECT
    COUNT(*)        AS total_orders,
    SUM(order_amount) AS total_revenue
FROM curated_orders;

-- 2. Payment success vs failure count
SELECT
    payment_status,
    COUNT(*) AS payment_count
FROM curated_payments
GROUP BY payment_status;


-- 3. Orders that do not have a successful payment
SELECT
    o.order_id,
    o.order_amount
FROM curated_orders o
LEFT JOIN curated_payments p
    ON o.order_id = p.order_id
    AND p.payment_status = 'SUCCESS'
WHERE p.order_id IS NULL;


-- 4. Revenue by region
SELECT
    region,
    SUM(order_amount) AS region_revenue
FROM curated_orders
GROUP BY region
ORDER BY region_revenue DESC;
