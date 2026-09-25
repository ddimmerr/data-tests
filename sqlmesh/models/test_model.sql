MODEL (
  name test_schema.test_model,
  kind FULL
);

SELECT
  1 AS id,
  'hello world' AS message
UNION ALL
SELECT
  2 AS id,
  'goodbye world' AS message