
import sys

genomesset = sys.argv[1]
k = int(sys.argv[2])
#unitigsfile = sys.argv[3]
unitig = sys.argv[3]

allunitigkmers = []
for i in range(len(unitig)-k+1):
    allunitigkmers.append(unitig[i:i+k])

f = open("occ_firstlast", "w")

f1 = open("occ_1", "w")
f2 = open("occ_2", "w")
f3 = open("occ_3", "w")
f4 = open("occ_4", "w")

with open(genomesset, 'r') as reader:
    line = reader.readline()

    while line != '':  # The EOF char is an empty string

        #print(line, end='')
        firstkmer = line[0:k]
        lastkmer = line[-k:]
        countf = 0
        countl = 0

        for i in range(len(line)-k+1):
            if (line[i:i+k] == firstkmer):
                countf += 1
            if (line[i:i+k] == lastkmer):
                countl += 1
        #countf = line.count(firstkmer)
        #countl = line.count(lastkmer)

        findindex_f = unitig.find(firstkmer)
        findindex_l = unitig.find(lastkmer)

        cond1 = True
        for uu in range(len(allunitigkmers)):
            if(line.find(allunitigkmers[uu])!=-1):
                cond1 = False
                break
        #cond1 = (findindex_f==-1 and findindex_l==-1)

        cond2 = False
        if(countf==1 and findindex_f>0):
            cond2 = True

        cond3 = False
        if(countl==1 and findindex_l<len(unitig)-k and findindex_l!=-1):
            cond3 = True

        cond4 = False
        if(countl==2 and countf==2 and findindex_l<len(unitig)-k and findindex_f>0 and findindex_l!=-1):
            cond4 = True

        # with open(unitigsfile, 'r') as unitigsfile_reader:
        #     unitig = unitigsfile_reader.readline()
        #     while unitig != '':
        #         if(countf==1):
        #             findindex = unitig.find(firstkmer)
        #             if(findindex!=-1):
        #                 if(findindex!=0):
        #
        #
        #         unitig = unitigsfile_reader.readline()
        #cond1:
        #if(countf==1):
        #counts = str(countf) + " " + str(countl) + "\n"
        counts = str(int(cond1)) + " " + str(int(cond2)) + " " + str(int(cond3)) + " " + str(int(cond4)) + "\n"
        f.write(counts)
        f1.write(str(int(cond1))+"\n")
        f2.write(str(int(cond2))+"\n")
        f3.write(str(int(cond3))+"\n")
        f4.write(str(int(cond4))+"\n")

        line = reader.readline()
f.close()
f1.close()
f2.close()
f3.close()
f4.close()
