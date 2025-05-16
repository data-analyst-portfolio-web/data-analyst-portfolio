-- Extract subscriber usage metrics
SELECT
    SubscriberID,
    DataUsedGB,
    VoiceMinutes,
    SMSCount
FROM
    dbo.Usage
WHERE
    UsageMonth >= '2024-01-01';
