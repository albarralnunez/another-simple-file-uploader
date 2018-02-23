#!/usr/bin/env bash

set -o errexit
set -o pipefail
set -o nounset


celery -A simple_file_uploader.taskapp beat -l INFO
