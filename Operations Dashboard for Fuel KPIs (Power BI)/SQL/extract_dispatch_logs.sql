
-- Extract Truck Dispatch Logs for Efficiency and Route Monitoring
SELECT
    dl.dispatch_id,
    dl.dispatch_date,
    dl.truck_id,
    dl.driver_id,
    d.driver_name,
    dl.start_location,
    dl.end_location,
    dl.start_time,
    dl.end_time,
    DATEDIFF(minute, dl.start_time, dl.end_time) AS duration_minutes,
    dl.distance_km,
    dl.fuel_used_liters,
    dl.idle_minutes,
    dl.delivery_count,
    t.truck_model
FROM
    dispatch_logs dl
JOIN
    drivers d ON dl.driver_id = d.driver_id
JOIN
    trucks t ON dl.truck_id = t.truck_id
WHERE
    dl.dispatch_date >= DATEADD(day, -30, GETDATE())
ORDER BY
    dl.dispatch_date DESC;
