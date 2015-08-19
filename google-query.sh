#!/bin/bash
# script sends question to google and prints result in case of QA
value=$1
encoded_value=$(python -c "import urllib; print urllib.quote_plus('''$value''',\"?\")")
result=$(curl -s -A Mozilla/5.0 "http://www.google.cz/search?q=$encoded_value&hl=en" | sed -ne 's/.*<span class="_m3b">\([^<]*\)<.*/\1/p')
if [ -z "$result" ]; then
	echo "no answer found"
else
	echo "$result"
fi