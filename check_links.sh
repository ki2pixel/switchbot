#!/bin/bash
for dir in .agents .windsurf; do
  find $dir -type f -name "*.md" | while read -r file; do
    grep -oE '\.(windsurf|agents)/[a-zA-Z0-9_/-]+\.md' "$file" | while read -r link; do
      if [ ! -f "$link" ]; then
        echo "Broken link in $file: $link"
      fi
    done
  done
done
echo "Check completed."
