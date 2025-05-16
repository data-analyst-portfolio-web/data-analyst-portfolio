-- Extract billing and cost data
SELECT
    SubscriberID,
    BillingMonth,
    Revenue,
    Cost
FROM
    dbo.Billing
WHERE
    BillingMonth >= '2024-01-01';
