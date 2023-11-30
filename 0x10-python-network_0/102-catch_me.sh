#!/bin/bash
# Get through to secret domain
curl -H 'Origin: HolbertonSchool' -sLX PUT -d user_id=98 "$1"
