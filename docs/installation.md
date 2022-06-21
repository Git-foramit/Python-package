## Installation

### Install from PyPI artifactory

To install the compiled version
from [AIBSE Artifactory](https://artifactory.boschdevcloud.com/ui/repos/tree/General/gs-pj-top98-ai-know-pypi-aibse-local)
, please open file `~/.pip/pip.conf` (`~` means your home directory, for example in Windows: C:\Users\YourNTAccount) and
put the following lines at the end:

````
[global]
index-url = https://anu9rng:AP6eY5xuhS1MqAdy5jedftw3ndQq7MHjXL8Rpb@rb-artifactory.bosch.com/artifactory/api/pypi/python-virtual/simple
trusted-host = pypi.org
extra-index-url = https://username:password@artifactory.boschdevcloud.com/artifactory/api/pypi/gs-pj-top98-ai-know-pypi-aibse-local/simple
https://username:password@artifactory.boschdevcloud.com/artifactory/api/pypi/lab000135-bios-bcai-pypi-local/simple
````

or when having Cntlm service running:

````
[global]
index-url = https://anu9rng:AP6eY5xuhS1MqAdy5jedftw3ndQq7MHjXL8Rpb@rb-artifactory.bosch.com/artifactory/api/pypi/python-virtual/simple
trusted-host = pypi.org
proxy=http://localhost:3128
extra-index-url = https://username:password@artifactory.boschdevcloud.com/artifactory/api/pypi/gs-pj-top98-ai-know-pypi-aibse-local/simple
https://username:password@artifactory.boschdevcloud.com/artifactory/api/pypi/lab000135-bios-bcai-pypi-local/simple
````

After that install aibse is as simple as running the command:

````python
pip install aibse
````

### Install from source

Clone a working branch (e.g. 0.4.0)

````python
git clone https://github.com/bosch-top98-ai-know/aibse-devkit.git --single-branch --branch 0.4.0
````

Then run the setup in your Python environment:

````python
cd aibse-devkit
python setup.py install
````

Or run pip in editable mode:

````python
cd aibse-devkit
pip install -e .
````

If you would like to *test* and *develop*, further installations are required:

````python
pip install pytest
pip install https://github.com/explosion/spacy-models/releases/download/de_core_news_md-2.3.0/de_core_news_md-2.3.0.tar.gz
````

_Note:_ There might be some more libraries missing. :-) Please report.

If you run into issues with Proxy or SSL, first set (with HTTPS_PROXY in capital letters on Windows):

````python
set HTTPS_PROXY=http://rb-proxy-de.bosch.com:8080
````
