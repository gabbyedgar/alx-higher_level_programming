#!/bin/bash
# Display the size of an HTTP request body
curl -so /dev/null -w '%{size_download}\n' "$1"
