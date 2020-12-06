#!/usr/bin/env python

import sys

from google.protobuf.compiler import plugin_pb2 as plugin


def generate_response(
    request: plugin.CodeGeneratorRequest, response: plugin.CodeGeneratorResponse
) -> None:

    # Loop over .proto files
    for proto_file in request.proto_file:
        pass


def main() -> None:
    # Load the CodeGeneratorRequest from stdin
    request = plugin.CodeGeneratorRequest.FromString(sys.stdin.buffer.read())

    # Create response
    response = plugin.CodeGeneratorResponse()

    # Generate code
    generate_response(request, response)

    # Serialize response message and write to stdout
    sys.stdout.buffer.write(response.SerializeToString())


if __name__ == "__main__":
    main()
