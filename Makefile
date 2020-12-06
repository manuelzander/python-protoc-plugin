.PHONY: all compile

all: compile

PLUGIN_PATH=./plugin.py
OUT_PATH=.

compile:
	chmod +x ${PLUGIN_PATH}
	protoc example.proto --plugin=protoc-gen-custom-plugin=${PLUGIN_PATH} --custom-plugin_out=${OUT_PATH} 
