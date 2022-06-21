# Changelog

Here lists all notable changes to this project

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres
to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [0.3.10]

### Added

- aibse.classifcation.eval (porting from aibse-prod -->analysis_utils)
- ndd.py with added code for building and loading ndd out of training loop
- integrating test cases from aibse-prod
- add improvement ratio into metrics.py

### Changed

- Preprocessing allow handling different splits now
- Fix several bugs in TrainContext due to changes of input from tokenizer_config to tokenizer_state
- Fix several bugs in mlflow artefact naming
- Fix several bugs in ArtifactManager

## [0.3.9]

### Added

- add model type in logged model output (model store) within "artifact_path" string (file "MLmodel")
- CCSpacyLM to encapsulates operations regarding embedding
- from_pretrain() to load pretrained model from external pretrained model store

### Changed

- update pretrain and train to facilitate the embedding
- move get_env() and create_path() back to general helper
- environment creation and activation is done now in global config yaml of enduser (local_mode).
- bugfix for inf_path in local_mode
- fix bug in create env in non-silent mode and activate
- jinja2 templateglobal_config_template without 'environment_names'.
- global config instantiated before Set_environ call.
- current_env accessed from aibse_config.yaml
- added property preprocessed_path into aibse_ctx

## [0.3.8]

### Changed

- aibse_config.yml removed from project folder, the global config gets created after the first yaml.dump is executed.
- environment creation and activation is done now in global config yaml of enduser (local_mode).
- bugfix for inf_path in local_mode

## [0.3.7]

### Changed

- add spacy model de_core_news_md

## [0.3.6]

### Changed

- restructure common packages
- add metrics (standard and cost model-based)
- fix bugs in AIBSEContext class, include AIBSE-INF
- add global_config_template and inf_path property.
- copy global config (aibse_config.yaml) inside AIBSE-INF (local mode).
- delivery of aibse_config.yaml inside aibse\configs

## [0.3.5]

### Changed

- fix bugs loading configs from global AIBSE-INF and environments
- rename from aibse_ctx.default_config --> config()
- fix bugs in update_config() (after updating self._config must be reassigned)
- remove the environment creation in AIBSEContext.init() (separation of concerns)

## [0.3.4]

### Changed

- fix bugs installing third party packages manually (Charsplit) and missing packages

## [0.3.3]

### Added

- Provide additional packaging directives to faciliate Conda (environment.yaml), Pipenv (Pipfile) and setuptools (
  setup.cfg)

### Changed

- refactor classifiers to aibse.classification

## [0.3.2]

### Added

- take mlflow utility APIs from pipelines 'attr_assign' to make them available to other projects (e.g. aibse-cli)

### Changed

- Training routines are extracted from pipelines 'attr_assign', made generic
- Port code from pipelines 'preprocessing' onto aibse.data.doors.csv as a default ETL

## [0.3.1]

### Added

- Update concept of context and configuration, reflect in documentation
  on [AIBSE toolkit runtime behaviour](https://inside-docupedia.bosch.com/confluence/display/TOP98/%282.6.2%29+Runtime+View+-+AIBSE+Toolkit)
- Set up
  local [JFrog PyPI artifactory](https://artifactory.boschdevcloud.com/ui/repos/tree/General/gs-pj-top98-ai-know-pypi-aibse-local)

### Changed

- Training routines are extracted from pipelines 'attr_assign', made generic
- Port code from pipelines 'preprocessing' onto aibse.data.doors.csv as a default ETL

## [0.3.0]

- Reduce concept of aibse-devkit to only Python SDK from the AIBSE Alpha concept
- Port code onto [Github](https://github.boschdevcloud.com/GS-PJ-TOP98-AI-KNOW/aibse-devkit.git) to enable CI/CD
- Adopt AI-KNOW documentation and project templates

### Removed

- pipelines, aibse-cli (put to separate projects)

## [0.2.0]

- [Experimental AIBSE Alpha](https://sourcecode.socialcoding.bosch.com/scm/top98/aibse-prod.git), active until Sprint
  15 (2021-06-30))
- Refine concepts in AIBSE Poc, break down 'components' into different types: Python SDK (aibse-toolkit) and pipelines

### Changed

- Refactor completely code structure, focus on reusability and reproducibility of the code

### Added

- Experimental model serving and inference (model-serving)
- Reimplement data preprocessing (ccdata) and classification (fnid_classifier) into configurable pipelines (pipelines)
- Command Line Interface for developer
- Build the generic AIBSE toolkit (aibse-toolkit)
- Set up concepts of end-user Command Line Interface (aibse-cli)

### Removed

- old ARieL code (data processing, frontend)
- data analysis notebooks
- evaluation notebooks
- data import of RAW DOORS export

## [0.1.0]

- [AIBSE PoC](https://sourcecode.socialcoding.bosch.com/scm/top98/aibse.git), activate until 2021-06-01
- Code is developed in different independent components

### Added

- Simple data ingestion from RAW DOORS CSV Exports using Powershell (data-import)
- Data Processing from DOORS CSV, extended from ARieL (ccdata)
- Data analysis in Jupyter notebooks (data-analysis)
- Baseline classification methods for attribute assignment (fnid_classifier)
- Evaluation under PoC 3 test cases, in Jupyter notebooks (evaluation)
- Copy of Web-based frontend developed in ARieL project (ariel-frontend)
- Experimental Jupyter notebooks with clustering methods (reqs_clustering)
