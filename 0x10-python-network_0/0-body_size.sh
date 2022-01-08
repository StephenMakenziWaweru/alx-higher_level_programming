#!/bin/bash
# sends a req to a URL and displays size of response
curl -sI $1 | awk '/content-length/ {print $2}'
