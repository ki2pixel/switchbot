#!/bin/bash
for dir in .agents .windsurf; do
  find $dir -type f -name "*.md" | while read -r file; do
    grep -oE '(references|assets|docs)/[a-zA-Z0-9_/-]+\.(md|sql)' "$file" | while read -r link; do
      # check if it's relative to the file's dir or project root
      file_dir=$(dirname "$file")
      if [ ! -f "$file_dir/$link" ] && [ ! -f "$link" ]; then
        echo "Broken link in $file: $link"
      fi
    done
  done
done
echo "Check completed."
