import cumulus_library


class CountConditionsBuilder(cumulus_library.CountsBuilder):
    def prepare_queries(
        self,
        *args,
        config: cumulus_library.StudyConfig,
        manifest: cumulus_library.StudyManifest,
        **kwargs,
    ):
        self.queries.append(
            # Since this is counting condition, the resulting table will
            # be a count of encounters associated with the condition.
            self.count_condition(
                table_name=f"{manifest.get_study_prefix()}__count_condition",
                source_table=f"{manifest.get_study_prefix()}__condition",
                table_cols=["code", "clinicalstatus_code"],
                # since the reference test data is small, we'll turn down the bin
                # size - but don't do this in a real study, or you'll potentially
                # have identifiable data sets
                min_subject=1,
            )
        )
