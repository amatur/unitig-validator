
# gap_len = 5
# gap_per = 1/1000
import random
import sys
import math

random.seed(1)

genomessetFile = sys.argv[1]
outFile = sys.argv[2]
coverage = int(sys.argv[3])
k=int(sys.argv[4])
read_len = 100


# genomessetFile = "test_ttt"
# outFile = "test_ttt_out"
# coverage = 1
# read_len = 2


wf = open(outFile,"w")
reads=[]

segfile=open("segfile.sset","w")
total_bp_all=0
num_reads_all=0

with open(genomessetFile) as f:
    gcount=0
    while True:
        gcount += 1

        # Get next line from file
        g = f.readline()

        # if line is empty
        # end of file is reached
        if not g:
            break

        g=g.rstrip()
        #print("Line{}: {}".format(count, g.strip()))

        '''
        g=f.read()
        g=g.rstrip()
        '''
        glist = list(g)
        total_bp = len(g)

        num_reads=math.ceil(coverage*total_bp/(read_len))

        ranlist_ind=[]
        if(total_bp<read_len):
            if(random.randint(0,1)==0):
                ranlist_ind.append(0)
        else:
            if(num_reads > total_bp-read_len):
                ranlist_ind=random.choices(range(0, total_bp-read_len), k=num_reads)
            else:
                ranlist_ind=random.sample(range(0, total_bp-read_len), num_reads)
        ranlist_ind.sort()
        #print(ranlist_ind)


        if(len(ranlist_ind)!=0):
            segs=[]
            same=False
            segstart=ranlist_ind[0]
            segend=ranlist_ind[0]+read_len-1
            for i in range(1,len(ranlist_ind)):

                if(segend - ranlist_ind[i] + 1 < k-1):
                    segs.append(g[segstart:segend+1])
                    segstart=ranlist_ind[i]
                    same=False
                    #segend=ranlist_ind[i]+read_len-1
                else:
                    same=True

                segend = ranlist_ind[i]+read_len-1
            segs.append(g[segstart:segend+1])

            for j in ranlist_ind:
                reads.append(g[j:j+read_len])
                wf.write(g[j:j+read_len]+"\n")

            for s in segs:
                segfile.write(s+"\n")

            total_bp_all+=total_bp
            num_reads_all+=num_reads


    segfile.close()
    wf.close()
    print("total_bp=",total_bp_all)
    print("coverage=",coverage,"x")
    print("num_reads=",num_reads_all)
    print("read_len=",read_len)
    print("num_seg=",len(segs))
