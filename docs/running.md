# Setting up the environment

Before running the code, you need to compile it and install the dependencies. Currently two platforms for environment
setup are supported:

### Setting up with Pipenv

Pipe Before running the code, you need to compile it and install the dependencies. To do this, use the make file and run
the following command in the root of the directory:

<div class="termy">

```console
$ make deps

Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Installing dependencies from Pipfile.lock (55c134)…

---> 100%

$ pipenv shell

```

</div>

or if you want to fully set up the dev mode (e.g. testing, linting,...):

<div class="termy">

```console
$ pipenv sync --dev

Courtesy Notice: Pipenv found itself running within a virtual environment, so it will automatically use that environment, instead of creating its own for any project. You can set PIPENV_IGNORE_VIRTUALENVS=1 to force pipenv to ignore that environment and create its own instead. You can set PIPENV_VERBOSITY=-1 to suppress this warning.
Installing dependencies from Pipfile.lock (55c134)…

---> 100%

$ pipenv shell

```

</div>

### Setting up with Conda

To build the Conda environment, run:

<div class="termy">

```console
$ conda env create -f environment.yml

---> 100%
```

</div>

Optionally, to write documentation and test locally, import extra libraries (mkdocs, mike) into the ``aibse-dev``
environment:

<div class="termy">

```console
$ pip install -r requirements-docs.txt

---> 100%
```

</div>

# Versioning

### Convention:

The versioning of aibse-devkit follows the semantic versioning change, with some adaptation to the AIBSE roadmap as
follows:

- v0.1 corresponds to the AIBSE development within the PoC (code
  base: <a href="https://sourcecode.socialcoding.bosch.com/projects/TOP98/repos/aibse/browse">aibse</a>)
- v0.2 corresponds to the AIBSE development prior to Github Enterprise port (code
  base: <a href="https://sourcecode.socialcoding.bosch.com/projects/TOP98/repos/aibse-prod/browse">aibse-prod</a>)
- v0.3 and later corresponds to the AIBSE development in Github Enterprise.

From v0.3 onwards, the semantic versioning convention will be adopted. This means a minor version now reflects the
inclusion of new features. For example, when adding a new feature to aibse-devkit  (e.g. deploying to the AI-KNOW
platform, new data preprocessing for further use cases such as linking), we should bump the version of aibse-devkit to
0.4.x, etc.

### Bumping versions:

The version of aibse-devkit is maintained in
the ``setup.cfg```. Alternatively, the changing of versions can be done programmatically using tool ``bumpversion``.
Please see <a href="https://github.boschdevcloud.com/GS-PJ-TOP98-AI-KNOW/web-service-template/">Web-serivce-template</a>
for more details about version bumping.

### Releasing versions:

The release of a version is done automatically, by handling the branch names (see below). During the release, the two
versioning scheme are supported in ``setup.py``. Please change the code accordingly

- Stable version:

```python
setup()
```

- Development version:

```python
setup(use_scm_version={"version_scheme": "python-simplified-semver"})
```

Please see <a href="https://github.com/pypa/setuptools_scm/">setuptools_scm</a> for more details.

# Branching Convention:

The CI/CD concept in AIBSE-dev requires some attention when creating or maintaining a branch:

- all branches started with ``releases/`` are reserved for release-ready code. The code under this branch will be
  scanned for linting, as well as automatic delivery of artefacts (PyPI packages).
- all branches started with ``features/`` or ``aiknow-`` are used to develop functionalities, fixing issues, e.g. the
  tasks described in <a href="https://rb-tracker.bosch.com/tracker19/secure/RapidBoard.jspa?rapidView=5202">JIRA
  board</a>. Code in this branch will be tested using continuous integration (CI) as soon as they are merged to
  the ``master`` branch, but Linting and CD actions are not applied here.
- all branches started with ``hotfixes/`` are reserved for short-lived development code to fix quick issues in the
  release.

The above concept is implemented in the Github actions accordingly. For example, when creating a new
branch ``releases/[next_version]``, all pushes and pull requests to this branch will result in a delivery of a new
artifact.
