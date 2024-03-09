
import re

print(sum( [ int(v) for v in re.findall('[0-9]+',open('../../data/sample/regex_sum_42.txt').read()) ] ))
