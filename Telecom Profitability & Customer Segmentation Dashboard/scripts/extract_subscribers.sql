-- Extract subscriber profile data
SELECT
    SubscriberID,
    Name,
    ContractType,
    Region,
    JoinDate,
    ARPU
FROM
    dbo.Subscribers
WHERE
    JoinDate >= '2022-01-01';
