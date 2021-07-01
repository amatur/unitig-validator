
gap_len = 5
gap_per = 1/1000

import sys

genomessetFile = sys.argv[1]
outFile = sys.argv[2]


wf = open(outFile,"w")

with open(genomessetFile) as f:
    g=f.read()
    glist = list(g)
    total_bp = len(g)
    gap_in = int(1/gap_per)

    j = gap_in
    while True:
        for m in range(gap_len):
            if(j+m<total_bp):
                glist[j+m] = 'N'
        j = j + gap_len +  gap_in
        if j >= total_bp:
            break
    g="".join(glist)
    wf.write(g)
    wf.close()
    print(total_bp, gap_len, gap_per, gap_in)
