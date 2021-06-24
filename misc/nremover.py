import re
import sys

f = open(sys.argv[1], "r")
txt = (f.read())
x = re.split("N+", txt)
megastr=[]
for i in x:
        ii = re.split("\n", i)
        for j in ii:
            megastr.append(j)

for i in megastr:
    if len(i)>0 and i!="\n":
        print(">contig")
        print(i)
