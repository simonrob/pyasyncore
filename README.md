[![No Maintenance Intended](http://unmaintained.tech/badge.svg)](http://unmaintained.tech/)

# Purpose
This package contains the [asyncore](https://docs.python.org/3/library/asyncore.html) module as found in Python versions prior to 3.12.
It is provided so that existing code relying on `import asyncore` is able to continue being used without significant refactoring.

The module's source code is taken directly from the [Python standard library](https://github.com/python/cpython/blob/c4d45ee670c09d4f6da709df072ec80cb7dfad22/Lib/asyncore.py).
The specific version of [`asyncore.py`](asyncore/asyncore.py) used is the last update before the addition of removal warnings at import time, and is essentially equivalent to [the version provided with Python 3.9](https://github.com/python/cpython/blob/3.9/Lib/asyncore.py).

Please note that new projects should prefer [asyncio](https://docs.python.org/3/library/asyncio.html).


## Installation and usage
This version of asyncore is intended for Python 3.12 or later.
It can be installed for earlier Python versions, but will have no effect, and the standard library version of asyncore will be used in its place.

Install the module using `pip`:
```shell
python -m pip install pyasyncore
```

Note that the [PyPi module](https://pypi.org/project/pyasyncore/) is named `pyasyncore` because creating modules with the same name as those provided by the standard library is not permitted.
Usage is still via `import asyncore`.

For guidance about using this module, see the [official documentation](https://docs.python.org/3/library/asyncore.html).


## Maintenance
Due to the fact that this module is [no-longer supported](https://peps.python.org/pep-0594/), no further maintenance of the code in [`asyncore.py`](asyncore/asyncore.py) is intended.
This project is only intended to be updated to make changes or improvements to the module packaging.


## License
[Python Software Foundation License Version 2](LICENSE)
