#usr/bin/bash
# Script takes  url sends a request display body size

if [ -z "$1" ]; then
	exit 1
fi
url="$1"
response=$(curl -s "$url")
size=${#response}
echo $size
