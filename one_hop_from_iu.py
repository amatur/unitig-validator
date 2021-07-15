import sys

gtouch = sys.argv[1] # actually invalids
k = int(sys.argv[2])

invalidnei=open("invalidnei.txt", 'w')
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
                invalidnei.write(toappend[0:k-1]+"A\n")
                invalidnei.write(toappend[0:k-1]+"C\n")
                invalidnei.write(toappend[0:k-1]+"G\n")
                invalidnei.write(toappend[0:k-1]+"T\n")
                invalidnei.write("A"+toappend[1:k]+"\n")
                invalidnei.write("C"+toappend[1:k]+"\n")
                invalidnei.write("G"+toappend[1:k]+"\n")
                invalidnei.write("T"+toappend[1:k]+"\n")
        line=reader.readline()
invalidnei.close()
