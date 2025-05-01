
-- Extract Tank Fill Logs for Monitoring Dashboard
SELECT
    t.fill_id,
    t.fill_date,
    t.tank_id,
    tk.site_id,
    tk.product_type,
    t.volume_filled_liters,
    t.operator,
    tk.max_capacity_liters,
    ROUND((t.volume_filled_liters / tk.max_capacity_liters) * 100, 2) AS fill_percent,
    s.site_name,
    s.region
FROM
    tank_fills t
JOIN
    tanks tk ON t.tank_id = tk.tank_id
JOIN
    sites s ON tk.site_id = s.site_id
WHERE
    t.fill_date >= DATEADD(day, -30, GETDATE())
ORDER BY
    t.fill_date DESC;
