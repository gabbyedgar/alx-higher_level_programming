#!/bin/bash
# Get allowed HTTP verbs
curl -sIX OPTIONS "$1" | awk -F': ' '/Allow/ { print $2 }'
