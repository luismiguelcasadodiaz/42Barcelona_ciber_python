The goal of the exercise is to learn how to **build** a package, **upload** it
to PyPI, and to install it with **pip**.

Exercise's instructions establish that package's name is my_minipack.

Inside PyPI, each package **MUST** have unique name.
From the user point of view is better than PyPI's package name and module name
at import sentence are equal.


This two facts moved me to define my module as:

> bcnlmcdminipack

To avoid collision wot other classmates exercises.

bcnlmcdminipack includes two modules:


. aprogress bar
. a logger.

The folder to build the package has this structure:


```
bcnlmcdminipack
|
|-- src/
|   |-- bcnlmcdminipack
|       |-- __init__.py
|       |-- logger.py
|       |-- progress.py
|-- tests/
|   |-- test_logger.py
|   |-- test_progress.py
|-- LICENSE
|-- README.md
|-- pyproject.toml
|-- requirements.txt
```

## __init__.py
In this file i metion all packages availabel from this module

```
from .loading import ft_progress
from .logger import LMCD_logger
```

Please, be aware of the dot ahead of files names.


I will use setuptools as build system. Other build systems are Flit, Poetry, 
disutils. Each build system has its own instructions for the configuration of pyproject.toml.

```
[build-system]
requires = ["setuptools>=61.0.0", "wheel"]
build-backend = "setuptools.build_meta"
```



With pip-compile from pip-tools
> python3 -m pip install pip-tools
> pip-compile --resolver=backtracking pyproject.toml 

I made a verification of toml file and generate a requirements.txt file.
I can install requirements with pip-sync

# Install locally
## Editable installs allow code edition after installation

In the folder wiht pyproject.toml file execute:

> python3 -m pip install -e .

# TestPyPI
There is an alternative repository for test purpouse. 
I created an account in it, enabled a 2FA and created an API Token 
for uploading packages. I saved the API token in $HOME/.pypirc


 # Build the package:
 Packages on PyPI are not plain text. They are wrapped.  
 
 Two formats to be used

 ## Source format
 It is a tar file compresed. It is more suitable for backups

 ## wheel format
 it is also a compressed file. it si more suitable for end users.

 The build command creates a dist folder to write the results

 > python -m build
 > Successfully built bcnlmcdminipack-0.0.1.tar.gz and bcnlmcdminipack-0.0.1-py3-none-any.whl


 Before uploadinf the package to the repository it is a good practice to check if fullfills requirements. 

 > twine check dist/bcnlmcdminipack-0.0.1.tar.gz
 >     Checking dist/bcnlmcdminipack-0.0.1.tar.gz: PASSED
 > twine check dist/bcnlmcdminipack-0.0.1-py3-none-any.whl
 >     Checking dist/bcnlmcdminipack-0.0.1-py3-none-any.whl: PASSED


 # Upload the package to PyPI

 > twine upload -r testpypi dist/*

 # Install the package from pyblic repository
 > pip install -i https://test.pypi.org/simple/ bcnlmcdminipack==0.0.1
