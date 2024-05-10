#usr/bin/bash
# Script takes  url sends a request,display size body of response
curl -s "$1" | wc -c
