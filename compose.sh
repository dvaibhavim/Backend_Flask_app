#!/usr/bin/env bash

CURRENT_DIR=$(dirname ${0})

if [ "${1}" == "dev" ]; then
  shift
  COMMAND="docker-compose -f docker-compose.yml -f docker-compose.dev.yml"
else
  COMMAND="docker-compose"
fi

if [ "${1}" == "run" ]; then
  shift
  COMMAND="${COMMAND} run --rm"
fi

${COMMAND} ${@}
