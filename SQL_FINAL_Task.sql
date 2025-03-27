-- Top 5 warehouses with highest average shipping time
SELECT warehouse_id, AVG(shipping_time_days) AS avg_shipping_time
FROM cleaned_data
GROUP BY warehouse_id
ORDER BY avg_shipping_time DESC
LIMIT 5;

-- Top 5 warehouses with the lowest stock levels
SELECT warehouse_id, SUM(current_stock) AS total_stock
FROM cleaned_data
GROUP BY warehouse_id
ORDER BY total_stock ASC
LIMIT 5;

-- Monthly order trends
SELECT DATE_FORMAT(monthly_sales, '%Y-%m') AS month, SUM(monthly_sales) AS total_orders
FROM cleaned_data
GROUP BY month
ORDER BY month;

-- Top 5 most sold product categories
SELECT product_category, SUM(monthly_sales) AS total_sold
FROM cleaned_data
GROUP BY product_category
ORDER BY total_sold DESC
LIMIT 5;

-- Total orders by location (assuming location represents region)
SELECT location AS region, COUNT(warehouse_id) AS total_orders
FROM cleaned_data
GROUP BY region
ORDER BY total_orders DESC;

-- Average shipping time by product category
SELECT product_category, AVG(shipping_time_days) AS avg_shipping_time
FROM cleaned_data
GROUP BY product_category
ORDER BY avg_shipping_time DESC;

SELECT warehouse, AVG(delivery_time) AS avg_delivery_time
FROM cleaned_data
GROUP BY warehouse
ORDER BY avg_delivery_time DESC
LIMIT 5;