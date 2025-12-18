CREATE TABLE template__encounter AS
WITH tmp_encounter AS (
    SELECT
        e.id,
        e.status,
        e.class_code,
        e.type_code,
        e.type_system,
        e.type_display,
        e.reasoncode_code,
        e.reasoncode_system,
        e.reasoncode_display,
        e.period_start_day,
        e.period_end_day,
        e.period_start_year,
        e.subject_ref,
        e.encounter_ref
    FROM core__encounter AS e, template__patient_cohort AS pc
    WHERE pc.subject_ref = e.subject_ref
)

SELECT
    e.id,
    e.status,
    e.class_code,
    e.type_code,
    e.type_system,
    e.type_display,
    e.reasoncode_code,
    e.reasoncode_system,
    e.reasoncode_display,
    e.period_start_day,
    e.period_end_day,
    e.period_start_year,
    e.subject_ref,
    e.encounter_ref
FROM tmp_encounter AS e, template__encounter_valueset AS ev
WHERE e.class_code = ev.code
