# python-protoc-example

![last-commit](https://img.shields.io/github/last-commit/manuelzander/python-protoc-example/main?logo=github&style=for-the-badge) ![issues-pr-raw](https://img.shields.io/github/issues-pr-raw/manuelzander/python-protoc-example?label=open%20prs&logo=github&style=for-the-badge) [![license](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

A basic skeleton for a custom Python plugin for protoc, Google's official compiler for [protobuf](https://github.com/protocolbuffers/protobuf).

>A plugin is just a program which reads a `CodeGeneratorRequest` protocol buffer from standard input and then writes a `CodeGeneratorResponse` protocol buffer to standard output. These message types are defined in [plugin.proto](https://developers.google.com/protocol-buffers/docs/reference/cpp/google.protobuf.compiler.plugin.pb). We recommend that all third-party code generators be written as plugins, as this allows all generators to provide a consistent interface and share a single parser implementation.

## Prerequisites

![python](https://img.shields.io/badge/python-3.9-blue?style=for-the-badge&logo=python&logoColor=white)

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

I ran and tested the code with Python 3.9 on macOS 10.15.7.

### Environment

Clone the repo to your local machine.

Create a virtual environment for Python 3 with:

    python3 -m pip install virtualenv
    python3 -m virtualenv env

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

Make sure the virtual environment is activated.

Run the code generation: 

    protoc example.proto --plugin=protoc-gen-custom-plugin=./plugin.py --custom-plugin_out=.

Note that `custom-plugin` is both the last portion of the plugin name and the first part of the out argument.

Or simply use the Makefile:

    make

## Authors

* Manuel Zander
