{{ config(materialized='view') }}

SELECT
    container_id,
    timestamp,
    temperature,
    humidity,
    vibration,
    commodity
FROM ATMOSYNC_DB.RAW.LIVE_SENSOR_DATA
WHERE temperature IS NOT NULL
  AND humidity IS NOT NULL