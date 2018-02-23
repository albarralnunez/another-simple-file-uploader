#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset
set -o xtrace


celery -A simple_file_uploader.taskapp worker -l INFO
