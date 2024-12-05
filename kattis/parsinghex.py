import re
import sys
for line in sys.stdin:
    for h in re.findall("0x[0-9a-f]+",line,re.IGNORECASE):
        print(h,int(h,base=0))
