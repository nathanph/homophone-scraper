#!/bin/bash
cat sorted.out | sed -e "s,\s*[\[\(].*,,g" -re "s,^ ,,g" > sorted_clean.out
grep -v -x -f sorted_clean.out english.txt > english_clean.txt
diff english_clean.txt english.txt > tmp.diff
cat tmp.diff | grep "> " | sed -re "s,^> ,,g"  > english.diff
rm tmp.diff
