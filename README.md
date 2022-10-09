# Raspberry Pi MQTT Client

[![codecov](https://codecov.io/gh/meinjens/raspi_mqtt_client/branch/main/graph/badge.svg?token=eeed6bff-8f29-4706-9e5d-02cfba116bc2)](https://codecov.io/gh/meinjens/raspi_mqtt_client)
[![CI](https://github.com/meinjens/raspi_mqtt_client/actions/workflows/main.yml/badge.svg)](https://github.com/meinjens/raspi_mqtt_client/actions/workflows/main.yml)

Awesome raspi_mqtt_client created by meinjens

## Install it from PyPI

```bash
pip install raspi_mqtt_client
```

## Usage

```py
from raspi_mqtt_client import BaseClass
from raspi_mqtt_client import base_function

BaseClass().base_method()
base_function()
```

```bash
$ python -m raspi_mqtt_client
#or
$ raspi_mqtt_client
```

## Development

Read the [CONTRIBUTING.md](CONTRIBUTING.md) file.

## Ingredients

- 📦 A basic [setup.py](setup.py) file to provide installation, packaging and distribution for your project.  
  Template uses setuptools because it's the de-facto standard for Python packages, you can run `make switch-to-poetry` later if you want.
- 🤖 A [Makefile](Makefile) with the most useful commands to install, test, lint, format and release your project.
- 📃 Documentation structure using [mkdocs](http://www.mkdocs.org)
- 💬 Auto generation of change log using **gitchangelog** to keep a HISTORY.md file automatically based on your commit history on every release.
- 🐋 A simple [Dockerfile](Dockerfile) to build a container image for your project.  
  `Containerfile` is a more open standard for building container images than Dockerfile, you can use buildah or docker with this file.
- 🧪 Testing structure using [pytest](https://docs.pytest.org/en/latest/)
- ✅ Code linting using [flake8](https://flake8.pycqa.org/en/latest/)
- 📊 Code coverage reports using [codecov](https://about.codecov.io/sign-up/)
- 🛳️ Automatic release to [PyPI](https://pypi.org) using [twine](https://twine.readthedocs.io/en/latest/) and github actions.
- 🎯 Entry points to execute your program using `python -m <python_demo>` or `$ python_demo` with basic CLI argument parsing.
- 🔄 Continuous integration using [Github Actions](.github/workflows/main.yml) with jobs to lint, test and release your project on Linux, Mac and Windows environments.
