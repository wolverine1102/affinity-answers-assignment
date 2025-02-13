#!/bin/bash

URL="https://www.amfiindia.com/spages/NAVAll.txt"
OUTPUT_FILE="scheme_data.tsv"

curl -s "$URL" | awk -F ';' 'NR > 1 && NF >= 5 { print $4 "\t" $5 }' > "$OUTPUT_FILE"
