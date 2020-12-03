# python-protoc-example

![last-commit](https://img.shields.io/github/last-commit/manuelzander/python-protoc-example/main?logo=github&style=for-the-badge) ![issues-pr-raw](https://img.shields.io/github/issues-pr-raw/manuelzander/python-protoc-example?label=open%20prs&logo=github&style=for-the-badge) [![license](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

An example for a Python plugin for protoc

## Prerequisites

![python](https://img.shields.io/badge/python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

The code is run and tested with Python 3.9 on macOS 10.15.7.

### Environment

Clone the repo to your local machine.

Create a virtual environment for Python 3 with:

    python3 -m pip install virtualenv
    python3 -m virtualenv -p python3 env

Activate the virtual environment with:

    source env/bin/activate

Install the required Python packages with:

    pip3 install -r requirements.txt

To install `protoc` (on Mac):

    brew install protobuf

Validate your installation with:

    protoc --version

The output should be `libprotoc 3.14.0` or similar.

On Linux you can use:

    apt install -y protobuf-compiler

## Run the example

    TBD

## Authors

* Manuel Zander
