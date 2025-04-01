#!/bin/bash

API_URL="http://127.0.0.1:8000/predict"

declare -a TESTS=(
  "I love this project!"
  "This is terrible."
  "I'm not sure how I feel about it."
  "Absolutely amazing experience."
  "Worst thing ever."
)

echo "Running sentiment tests..."

for text in "${TESTS[@]}"; do
  echo -e "\nInput: $text"
  curl -s -X POST "$API_URL" \
    -H "Content-Type: application/json" \
    -d "{\"text\": \"$text\"}" | jq
done

