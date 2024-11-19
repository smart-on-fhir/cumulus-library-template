# Cumulus Library Study Template

This project aims to give you a forkable repository you can use for creating
clinical studies with 
[Cumulus Library](https://github.com/smart-on-fhir/cumulus-library).

## How do I customize this project?

Here's what we recommend:

- Pick a name for your study. 
- Rename the `cumulus-library-template` folder. This will match the name used
    to install packages with pip. It may match your study name, but it does not
    have to. We recommend keeping the `cumulus-library` prefix, but you don't 
    have to - just make sure your project documentation references the Cumulus 
    Library in some way.
- Follow the comment instructions in `pyproject.toml` and `manifest.toml` to
    set up these files to work with Cumulus Library.
- When invoking with `cumulus-library`, use the `--study_dir` flag to point to
    the directory containing the `manifest.toml`, or use the
    `CUMULUS_LIBRARY_STUDY_DIR` env var to a filepath which contains your study
    directory. The `--study-dir` flag will check subdirectories for you.