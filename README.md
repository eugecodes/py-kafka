# Lifecycle - Python SDK

[![Codacy Badge]()

## Overview

The SDK takes the responsibility of generating schema compliant notifications across functional services.
The library only provides with the message generation and does not have the capability to send it to an event bus.
This is a strategic decision as event hubs integration are already present in almost all services and exported as common
library.

## Consuming the Library

### Configure jFrog Artifactory for Pip Install
```
$ pip install frog-bar -i http://<username>:<password>@localhost:8081/artifactory/api/pypi/pypi-local/simple
```

~/.pip/pip.conf

[global]
index-url = http://user:password@localhost:8081/artifactory/api/pypi/pypi-virtual/simple


### To install
```py
source venv/bin/activate
pip install -r requirements.txt
pip install lifecycle
```

### How to add the library to a python project

Include this dependency to use the library.

```py
import lifecycle
from lifecycle import notification
```

## Building the Library


### To run tests
```py
python setup.py pytest
```

### To build the library
```py
python setup.py bdist_wheel
```

### To install the library
```py
pip install /dist/lifecycle-0.1.0-py3-none-any.whl
```

## Generating notification

A notification message has two parts

1.header

2.payload
