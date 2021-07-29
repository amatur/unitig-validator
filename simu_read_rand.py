
# gap_len = 5
# gap_per = 1/1000
import random
import sys
import math

random.seed(1)

genomessetFile = sys.argv[1]
outFile = sys.argv[2]
coverage = int(sys.argv[3])
#read_len = int(sys.argv[4])
read_len = 100
#gap_per=1.0/gap_freq


wf = open(outFile,"w")
reads=[]

with open(genomessetFile) as f:
    g=f.read()
    g=g.rstrip()
    glist = list(g)
    total_bp = len(g)

    num_reads=math.ceil(coverage*total_bp/(read_len))

    ranlist_ind=random.sample(range(0, total_bp-read_len), num_reads)
    #print(ranlist_ind)


    for j in ranlist_ind:
        reads.append(g[j:j+read_len])
        wf.write(g[j:j+read_len]+"\n")


    wf.close()
    print("total_bp=",total_bp)
    print("coverage=",coverage,"x")
    print("num_reads=",num_reads)
    print("read_len=",read_len)
