import sys

k=int(sys.argv[2])
gtouch=sys.argv[1]

out = open("out.html","w")
out.write("<html>")
out.write("<body>")

with open(gtouch, 'r') as reader:
    line = reader.readline()
    out.write("<p>")
    oldinvalid=""
    flag=False
    if line=='':
        out.write("</p>")
    while line != '':  # The EOF char is an empty string
        line=line.rstrip()
        linesplit = line.split()
        invaliduni = linesplit[0].rstrip()
        if(invaliduni!=oldinvalid):
            flag=True
        if(flag):
            out.write("</p>")
            out.write("<p>")
            bb=""
            rr=""
            pp=""
            kk=""
            if(len(invaliduni)>=2*k):
                bb=invaliduni[0:k]
                kk=invaliduni[k:len(invaliduni)-k]
                rr=invaliduni[len(invaliduni)-k:]
            else:
                bb=invaliduni[0:len(invaliduni)-k]
                pp=invaliduni[len(invaliduni)-k:k]
                rr=invaliduni[k:len(invaliduni)]
            #out.write("<u>"+invaliduni+"</u><br>")
            out.write("<u><span style='color:blue;'>{0}</span><span style='color:black;'>{1}</span><span style='color:purple;'>{2}</span><span style='color:red;'>{3}</span></u><br>".format(bb, kk, pp, rr))
            flag=False
        oldinvalid=invaliduni

        g = linesplit[1].rstrip()
        firstkmer = invaliduni[0:k]
        lastkmer = invaliduni[len(invaliduni)-k:]

        line = reader.readline()

        l_start = g.find(lastkmer)
        f_start = g.find(firstkmer)

        if (not (l_start==-1 or f_start==-1 or l_start <= f_start)):
            print("WARNING: u_m should appear before u_0 in an invalid unitig!")

        bluetext=""
        redtext=""
        purpletext=""
        p1=""
        p2=""
        p3=""
        #f_start+k-1 >= l_start
        if(f_start!=-1 and l_start!=-1 and f_start <= l_start+k-1):
            p1=g[0:l_start]
            redtext=g[l_start:f_start]
            purpletext=g[f_start:l_start+k]
            bluetext=g[l_start+k:f_start+k]
            p3=g[f_start+k:]
        elif(f_start!=-1 and l_start!=-1 and f_start > l_start+k-1 ):
            p1=g[0:l_start]
            redtext=g[l_start:l_start+k]
            p2=g[l_start+k:f_start]
            bluetext=g[f_start:f_start+k]
            p3=g[f_start+k:]
        elif(f_start!=-1 and l_start==-1):
            p1=g[0:f_start]
            bluetext=firstkmer
            p3=g[f_start+k:]
        elif(f_start==-1 and l_start!=-1):
            p1=g[0:l_start]
            redtext=lastkmer
            p3=g[l_start+k:]
        else:
            p1=g
        out.write("<span style='color:black;'>{0}</span><span style='color:red;'>{1}</span><span style='color:purple;'>{2}</span><span style='color:black;'>{3}</span><span style='color:blue;'>{4}</span><span style='color:black;'>{5}</span><br>".format(p1, redtext, purpletext, p2, bluetext, p3))
#0+1+        2+      3   4       5
#p1+redtext+purpletext+p2+bluetext+p3




out.write("</body>")
out.write("</html>")

out.close()

