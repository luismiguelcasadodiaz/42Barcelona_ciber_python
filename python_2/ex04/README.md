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
 
