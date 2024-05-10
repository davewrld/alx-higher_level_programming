#!/bin/bash
# sends request to URL.Dispalys status code
curl -s -o /dev/null -w "%{http_code}" "$1"
