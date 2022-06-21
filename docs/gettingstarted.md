# Getting Started

Please see [Prerequisites](prerequisites.md) to see the requirements for running aibse-devkit.

AIBSE-Devkit consists of list of modules and packages that can be reused in several applications and services in AIBSE.
Consider putting a module from the other projects if you think you need it beyond your project.

## [Installation](installation.md)

## Project Structure

### Common non-code files

The following files are used for setting up, testing, deploying the projects. They can be copied and adapted to other
AIBSE projects as well. Please
see [Web service template](https://pages.github.com/bosch-top98-ai-know/web-service-template)
for detailed usages of the files below.

Files and Folders                 | Purpose
--------------------------------- | ----------------------------------
``./docs``                        | user documentation, see [documentation](documentation.md)
``./Pipfile``                     | requirements for Pipenv users, see [setting up environment](running.md)
``./Pipfile.lock``                | pinned requirements for Pipenv users, see [setting up environment](running.md)
``./environment.yml``             | requirements for Conda users, see [setting up environment](running.md)
``./requirements-docs.txt``       | requirements to test the mkdocs locally
``./tests``                       | the test suite, see [tests](tests.md)
``.github``                       | CI/CD related files
``./LICENSE``                     | license and copyright
``./README.md``                   | developer documentation
``./setup.py``                    | setup script for packaging (setuptools)
``./setup.cfg``                   | package configuration
``./MANIFEST.in``                 | including extra files into PyPI artifact, see [instruction](https://packaging.python.org/guides/using-manifest-in/).
``./Makefile``                    | scripts to generate related artefacts (docs,...) in Linux environment
``./pre-commit-config.yaml``      | Configuration file for pre-commits library
``./bumpversion.cfg``             | Configuration file for bumpversion library
``./CHANGELOG.md``                | Description of the changes and versioning

### Code files

(For details, see [architecture](architecture.md)).

Files and Folders                 | Purpose
--------------------------------- | ----------------------------------
``./aibse/*.py``                  | common modules in AIBSE-devkit
``./aibse/nlp``                   | modules for handling the NLP of requirements
``./aibse/data``                  | modules to process ETL logics of requirement data sources (DOORS, DOORS export,..)
``./aibse/classification``        | modules developed in assignment attributes use-case, that can be used in general text classification in AIBSE as well
``./aibse/v1``                    | new APIs for aibse-devkit v1.x . Currently kept separate for backward-compatibility
``./aibse/configs``               | default constants in AIBSE applications and services configuration
