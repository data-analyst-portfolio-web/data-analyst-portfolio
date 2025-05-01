
-- Extract Delivery Records for Summary Reporting
SELECT
    d.delivery_id,
    d.delivery_date,
    d.truck_id,
    d.customer_id,
    c.customer_name,
    d.fuel_type,
    d.volume_liters,
    d.scheduled_time,
    d.actual_delivery_time,
    CASE 
        WHEN d.actual_delivery_time <= d.scheduled_time THEN 'On Time'
        ELSE 'Late'
    END AS status,
    d.region,
    d.site_id
FROM
    deliveries d
JOIN
    customers c ON d.customer_id = c.customer_id
WHERE
    d.delivery_date BETWEEN DATEADD(month, -1, GETDATE()) AND GETDATE()
ORDER BY
    d.delivery_date DESC;
