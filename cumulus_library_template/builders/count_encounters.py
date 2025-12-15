import cumulus_library


class CountEncounterBuilder(cumulus_library.CountsBuilder):
    def prepare_queries(
        self,
        *args,
        config: cumulus_library.StudyConfig,
        manifest: cumulus_library.StudyManifest,
        **kwargs,
    ):
        self.queries.append(
            # Since this is counting encounters, the resulting table will
            # be a count of patients for each encounter type.
            self.count_encounter(
                table_name=f"{manifest.get_study_prefix()}__count_encounter",
                source_table=f"{manifest.get_study_prefix()}__encounter",
                table_cols=["class_code", "period_start_year"],
                # this will add additional fields that are treated as metadata
                # labels, rather than part of a powerset
                annotation=cumulus_library.CountAnnotation(
                    field="class_code",
                    join_table=f"{manifest.get_study_prefix()}__encounter_valueset",
                    join_field="code",
                    columns=[("display", None)],
                ),
            )
        )
