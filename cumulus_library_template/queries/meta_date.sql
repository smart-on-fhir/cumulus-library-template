CREATE TABLE template__meta_date AS
WITH valid_period AS (
    SELECT DISTINCT
        e.period_start_day,
        e.period_end_day
    FROM
        template__encounter AS e
)

SELECT
    min(period_start_day) AS min_date,
    max(period_end_day) AS max_date
FROM valid_period;
