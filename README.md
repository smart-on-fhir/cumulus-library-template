# Cumulus Library Study Template

This project aims to give you a forkable repository you can use for creating
clinical studies with 
[Cumulus Library](https://github.com/smart-on-fhir/cumulus-library),
along with some examples of how to create tables

## How do I get started?

Here's what we recommend:

- Pick a name for your study (e.g. `your-study`) This name is how it will appear in the 
  Cumulus dashboard. You will also need a package name - `cumulus-library-your-study`
  is what we usually chose. Just make sure it's a unique python package name.
  You'll use dashes in the package name in pyproject.toml, and underscores elsewhere
- Rename the `cumulus_library_template` folder to match your package name  
- Change this line in `.github/workflows/ci.yaml`:
  ```python
  python -m pytest --cov-report xml --cov=cumulus_library_template tests
  ```
  to point to your new package name

- Follow the comment instructions in `pyproject.toml` and `manifest.toml` to
    set up these files to work with Cumulus Library.
- When invoking with `cumulus-library`, use the `--study_dir` flag to point to
    the directory containing the `manifest.toml`, or use the
    `CUMULUS_LIBRARY_STUDY_DIR` env var to a filepath which contains your study
    directory. The `--study-dir` flag will check subdirectories for you.

We also suggest the following:

- Install the dev dependencies with `pip install [.dev]`
- Run `pre-commit install` to install the pre-commit hooks, which will auto
  run linters before you push a commit
- We have CI actions for running linters and unit tests as validation in github,
  which will run with no additional configuration

The example study includes some sample files that will build a functioning study,
which you can use as a reference for starting. For more information, see the
[Example docs](./docs/example.md)