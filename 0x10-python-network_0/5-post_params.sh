#!/bin/bash
# Post some data to a web server
curl -sd 'email=hr@holbertonschool.com&subject=I will always be here for PLD' "$1"
