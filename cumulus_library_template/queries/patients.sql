CREATE TABLE template__patient_cohort AS
SELECT
    id,
    birthdate,
    gender,
    subject_ref
FROM core__patient
WHERE birthdate >= DATE '2000-01-01' AND birthdate <= DATE '2026-01-01'
