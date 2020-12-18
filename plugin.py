#!/usr/bin/env python

import json
import logging
import sys

from google.protobuf.compiler import plugin_pb2 as plugin
from google.protobuf.descriptor_pb2 import FileDescriptorProto


logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


def process_file(
    proto_file: FileDescriptorProto, response: plugin.CodeGeneratorResponse
) -> None:
    logger.info(f"Processing proto_file: {proto_file.name}")

    # Create dict of options
    options = str(proto_file.options).strip().replace("\n", ", ").replace('"', "")
    options = dict(item.split(": ") for item in options.split(", ") if options)  # type: ignore

    # Create list of dependencies
    dependencies = list(proto_file.dependency)

    data = {
        "package": f"{proto_file.package}",
        "filename": f"{proto_file.name}",
        "dependencies": dependencies,
        "options": options,
    }

    f = response.file.add()
    f.name = proto_file.name + ".json"
    logger.info(f"Writing file: {f.name}")
    f.content = json.dumps(data, indent=2) + "\r\n"


def process(
    request: plugin.CodeGeneratorRequest, response: plugin.CodeGeneratorResponse
) -> None:

    # Loop over .proto files
    for proto_file in request.proto_file:
        process_file(proto_file, response)


def main() -> None:
    # Load the request from stdin
    request = plugin.CodeGeneratorRequest.FromString(sys.stdin.buffer.read())

    # Create a response
    response = plugin.CodeGeneratorResponse()

    process(request, response)

    # Serialize response and write to stdout
    sys.stdout.buffer.write(response.SerializeToString())


if __name__ == "__main__":
    main()
