import re
import sys

txt = sys.argv[1]
k = int(sys.argv[2])

for i in range(len(txt)-k+1):
    print(txt[i:i+k])

