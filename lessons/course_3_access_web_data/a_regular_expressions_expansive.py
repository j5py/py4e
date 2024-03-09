
# In this assignment you will read through and parse a file with text and numbers

    # Cheat Sheet: https://www.py4e.com/lectures3/Pythonlearn-11-Regex-Handout.txt

import re

try:
    handle = open('regex_sum_42.txt')
except:
    handle = open('../../data/sample/regex_sum_42.txt')


# You will extract all the numbers in the file and compute the sum of the numbers
    
count = 0

for line in handle:
    integers = re.findall('[0-9]+', line)
    for key in integers:
        count += int(key)

print(count)
