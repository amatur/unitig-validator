import sys

gtouch = sys.argv[1] # actually invalids
k = int(sys.argv[2])
outfile= sys.argv[3]

invalidnei=open(outfile, 'w')
with open(gtouch, 'r') as reader:
    #lobal currvindex
    line = reader.readline()

    if line=="":
        print("done")

    while line != "":  # The EOF char is an empty string
        invaliduni=line.rstrip()
        if(1==1):
            for i in range(len(invaliduni)-k+1):
                toappend = invaliduni[i:i+k]
                invalidnei.write("A"+toappend[0:k-1]+"\n")
                invalidnei.write("C"+toappend[0:k-1]+"\n")
                invalidnei.write("G"+toappend[0:k-1]+"\n")
                invalidnei.write("T"+toappend[0:k-1]+"\n")
                invalidnei.write(toappend[1:k]+"A\n")
                invalidnei.write(toappend[1:k]+"C\n")
                invalidnei.write(toappend[1:k]+"G\n")
                invalidnei.write(toappend[1:k]+"T\n")
        line=reader.readline()
invalidnei.close()
