#!/usr/bin/env bash

location="/Users/bra17/Documents/workspace/GIT/netcomm1/"
api_file="openapi/spec.yaml"
project_dir="flaskgen"
project_src="src"

echo "swagger_py_codegen -s $location$api_file $location$project_dir  -p $project_src"
swagger_py_codegen -s $location$api_file $location$project_dir  -p $project_src
