import sys
import os

KMER_FILE=(sys.argv[1]) # "iu_mers71"
INVALID_UNITIG_FILE=sys.argv[2] # unid71.sset
SEG_FILE=sys.argv[3] # segfile.sset
PAIR_FILE=sys.argv[4]  #pair

#kmer_to_contignum=dict()
kmer_to_unitig_id=dict()
contignum_to_kmer=dict()

#seg_to_contignum=dict()
contignum_to_seg=dict()
unitigs=[]

k=0
contigstr_kmer=""
with open(KMER_FILE, 'r') as reader:
    line = reader.readline()
    while line != '':
        kmer = line.rstrip()
        if (kmer[0] == '>'):
            contigstr_kmer=kmer[1:]
        if (kmer[0] != '>'):
            #kmer_to_contignum[kmer] = contigstr_kmer
            contignum_to_kmer[contigstr_kmer] = kmer
            k=len(kmer)
        line = reader.readline()

contigstr_seg=""
with open(SEG_FILE, 'r') as reader:
    line = reader.readline()
    while line != '':
        seg = line.rstrip()
        if (seg[0] == '>'):
            contigstr_seg=seg[1:]
        if (seg[0] != '>'):
            #seg_to_contignum[seg] = contigstr_seg
            contignum_to_seg[contigstr_seg] = seg
        line = reader.readline()

uid=0
with open(INVALID_UNITIG_FILE, 'r') as reader:
    line = reader.readline()
    while line != '':
        u = line.rstrip()
        if (u[0] != '>'):
            unitigs.append(u) #uid
            for i in range(len(u) - k + 1):
                kmer_to_append = u[i:i + k]
                kmer_to_unitig_id[kmer_to_append] = uid
            uid += 1

        line = reader.readline()


gtouch_out=open("gtouch", "w")
with open(PAIR_FILE, 'r') as reader:
    line = reader.readline()
    while line != '':
        linesplit = line.rstrip().split('\t')
        unitig = unitigs[kmer_to_unitig_id[contignum_to_kmer[linesplit[0]]]]
        segment = contignum_to_seg[linesplit[1]]
        gtouch_out.write(unitig+" "+segment+"\n")
        line = reader.readline()

