#!/bin/bash
# takes a URL, sends GET, dispalays body of the response
curl -sL "$1" | grep -q 'HTTP/200' && cat -
