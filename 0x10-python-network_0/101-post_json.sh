#!/bin/bash
# POST a JSON file to web server
curl -sH "Content-Type: application/json" -d "@$2" "$1"
