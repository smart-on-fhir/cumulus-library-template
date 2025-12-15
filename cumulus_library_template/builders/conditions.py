import cumulus_library
from cumulus_library.template_sql import base_templates


class CondtionBuilder(cumulus_library.BaseTableBuilder):
    def prepare_queries(
        self,
        *args,
        config: cumulus_library.StudyConfig,
        manifest: cumulus_library.StudyManifest,
        **kwargs,
    ):
        self.queries.append(
            base_templates.get_create_table_from_tables(
                table_name=f"{manifest.get_study_prefix()}__condition",
                tables=[
                    f"{manifest.get_study_prefix()}__patient_cohort",
                    "core__condition",
                ],
                table_aliases=["pc", "c"],
                columns=[
                    "c.code",
                    "c.system",
                    "c.code_display",
                    "c.recordeddate",
                    "c.subject_ref",
                    "c.encounter_ref",
                    "c.condition_ref",
                    "c.clinicalstatus_code",
                ],
                join_clauses=["c.subject_ref = pc.subject_ref"],
            )
        )
