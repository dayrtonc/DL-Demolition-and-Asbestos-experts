#!/bin/bash

# Google Analytics code to be inserted
GA_CODE='  <!-- Google tag (gtag.js) -->\n  <script async src="https://www.googletagmanager.com/gtag/js?id=G-4GBXQJ78CT"></script>\n  <script>\n    window.dataLayer = window.dataLayer || [];\n    function gtag(){dataLayer.push(arguments);}\n    gtag('\''js'\'', new Date());\n    gtag('\''config'\'', '\''G-4GBXQJ78CT'\'');\n  </script>'

# Find all HTML files (excluding backup directory)
find . -maxdepth 1 -name "*.html" -type f | while read file; do
  # Check if GA code is already present
  if ! grep -q "G-4GBXQJ78CT" "$file"; then
    # Insert GA code after <head> tag
    sed -i "/<head>/a\\
$GA_CODE" "$file"
    echo "Added GA to: $file"
  else
    echo "GA already exists in: $file"
  fi
done

echo "Google Analytics installation complete!"
