#usr/bin/bash
# Script takes  url sends a request,display size body of response
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2
