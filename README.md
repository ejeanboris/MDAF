

**MDAF**
======================

**Overview**
------------

The MDAF (Multi-Disciplinary Analysis Framework) repository provides a collection of tools and functions for performing multi-disciplinary analysis, optimization, and surrogate modeling.

**Installation**
---------------

To install the MDAF package, use the following command:

```bash
pip install git+fullurl
```

**Dependencies**
---------------

The MDAF package depends on the following libraries:

* `rpy2`
* `scikit-learn`
* `numpy`
* `matplotlib`

**Usage**
-----

The MDAF package provides several functions and tools for performing multi-disciplinary analysis, optimization, and surrogate modeling. Some examples include:

* `installFlacco`: Installs the Flacco package and its dependencies.
* `representfunc`: Represents test functions for analysis and optimization.
* `doe`: Performs design of experiments (DOE) for surrogate modeling.

**Test Functions**
-----------------

The MDAF package includes a collection of test functions for analysis and optimization, including:

* `Alpine.py`
* `Bukin4.py`
* `Bukin6.py`
* `Keane.py`
* `Leon.py`
* `Miele_Cantrell.py`
* `Rastriring.py`
* `Step.py`
* `Step2.py`
* `Wayburn.py`
* `Zettle.py`
* `Zirilli.py`

**Notebooks**
------------

The repository includes several Jupyter notebooks that demonstrate the usage of the MDAF package, including:

* `Analyse_folders_and_description.ipynb`
* `PSO.ipynb`
* `Simulated_Annealing_General.ipynb`

**Tests**
--------

The repository includes a collection of unit tests and integration tests to ensure the correctness of the MDAF package.


## Misc
- reinstall the package for testing: 
```bash
py -m pip install --upgrade --force-reinstall git+fullurl
```

- use specific versions: `python 37`

- dependencies: `rpy2, scikitlearn, `

- Windows: install R first
    - When using installFlacco please choose to create a new library on the first run


