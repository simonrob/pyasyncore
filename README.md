[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

# Purpose
This package contains the [asyncore](https://docs.python.org/3.11/library/asyncore.html) module as found in Python versions prior to 3.12.
It is provided so that existing code relying on `import asyncore` is able to continue being used without significant refactoring.

The module's source code is taken directly from the [Python standard library](https://github.com/python/cpython/blob/c4d45ee670c09d4f6da709df072ec80cb7dfad22/Lib/asyncore.py)<sup id="a1">[[1]](#f1)</sup>.
The specific version of [`asyncore.py`](asyncore/asyncore.py) that is provided is the last update before the addition of deprecation/removal warnings at import time, and is essentially equivalent to [the version bundled with Python 3.9](https://github.com/python/cpython/blob/3.9/Lib/asyncore.py).

Please note that new projects should prefer [asyncio](https://docs.python.org/3/library/asyncio.html).


## Installation
This version of `asyncore` is intended for Python 3.12 or later. Install the module using `pip`:
```shell
python -m pip install pyasyncore
```

The module can be installed for earlier Python versions, but it will have no effect, and the standard library version of `asyncore` will be used in its place.

Note that installing `pyasyncore` will not remove deprecation warnings in Python versions 3.10 and 3.11.
Instead, use the `warnings` package:
```python
import warnings
with warnings.catch_warnings():
    warnings.simplefilter('ignore', DeprecationWarning)
    import asyncore
```


## Usage
The module is imported in exactly the same way as the standard library component it replaces:
```python
import asyncore
```

Note that the [PyPI module](https://pypi.org/project/pyasyncore/) is named `pyasyncore` because creating modules with the same name as those provided by the standard library is not permitted.

For guidance about using the `asyncore` module, see the [official documentation](https://docs.python.org/3.11/library/asyncore.html).


## Maintenance
Due to the fact that this previously built-in module is [no-longer supported](https://peps.python.org/pep-0594/) by the Python core development team, no further maintenance of the code in [`asyncore.py`](https://github.com/simonrob/pyasyncore/blob/master/setup.py) is intended.
This project is only intended to be updated to make changes or improvements to the module packaging.


## License
[Python Software Foundation License Version 2](LICENSE)


### Footnotes
<sub id="f1">1. Verify this if needed via: `diff <(curl --location https://github.com/python/cpython/raw/c4d45ee670c09d4f6da709df072ec80cb7dfad22/Lib/asyncore.py) <(curl --location https://github.com/simonrob/pyasyncore/raw/master/asyncore/asyncore.py)` [⏎](#a1)</sub>
