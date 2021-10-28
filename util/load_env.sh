#!/bin/bash
# Execute this script like so: source load_env.sh in order to load the environment variables in the current bash shell.
# Credit: https://gist.github.com/mihow/9c7f559807069a03e302605691f85572

# The .env file containing all the environment variables to export, will be located in the root of the repository.
ENV_FILE=$PWD/../.env

# Loads the environment variables set in the file $ENV_FILE as environment variables.
set -a; source $ENV_FILE; set +a
