import sys

gtouch = sys.argv[1]
k = int(sys.argv[2])

#ref = sys.argv[3]
colors=["black","white","aqua","blue","blueviolet","brown","burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue","cornsilk","crimson","darkblue","darkorchid","aquamarine","cyan","darkcyan","darkgoldenrod","darkgray","darkgreen","darkkhaki","darkmagenta","darkolivegreen","darkorange","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray","darkturquoise","darkviolet","deeppink","deepskyblue","dimgray","dodgerblue","firebrick","forestgreen","fuchsia","gainsboro","gold","goldenrod","gray","green","greenyellow","hotpink","indianred","indigo","khaki","lavender","lavenderblush","lawngreen","lemonchiffon","lightblue","lightcoral","lightcyan","lightgoldenrodyellow","lightgray","lightgrey","lightpink","lightsalmon","lightseagreen","lightskyblue","lightslategray","lightsteelblue","lightyellow","limegreen","linen","magenta","maroon","mediumaquamarine","mediumblue","mediumorchid","mediumpurple","mediumseagreen","mediumslateblue","mediumspringgreen","mediumturquoise","mediumvioletred","midnightblue","mintcream","mistyrose","moccasin","navajowhite","navy","oldlace","olive","olivedrab","orange","orangered","orchid","palegoldenrod","palegreen","paleturquoise","palevioletred","papayawhip","peachpuff","peru","pink","plum","powderblue","rosybrown","royalblue","saddlebrown","salmon","sandybrown","seagreen","sienna","silver","skyblue","slateblue","slategray","springgreen","steelblue","tan","teal","thistle","tomato","turquoise","violet","wheat","yellow","yellowgreen"]

allunitigkmers = dict()
id_to_seq = dict()
sdict = dict()
pdict = dict()
gr=dict()
currvindex=0
startofblack=0

kmomerd=dict()

indegree=[]
outdegree=[]


firsts=[]
lasts=[]

genomefirst={}
genomelast={}


tosearchinref=[]

refstr=""

issampled={}
isstart_of_inu={}
isend_of_inu={}

genomedict={}
genomes=[]
vertex_to_genomeid={}

def find_all(a_str, sub):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1: return
        yield start
        start += 1 # use start += 1 to find overlapping matches
# print(list(find_all('ATATAT', 'ATAT')))


genomeid=0
with open(gtouch, 'r') as reader:
    line = reader.readline()
    oldinvalid=""
    flag=False
    if line=='':
        print("done")

    while line != '':  # The EOF char is an empty string
        line=line.rstrip()
        linesplit = line.split()
        invaliduni = linesplit[0].rstrip()
        if(invaliduni!=oldinvalid):
            flag=True
        if(flag):
            if(oldinvalid==""):
                print("start")
            for i in range(len(invaliduni)-k+1):
                toappend = invaliduni[i:i+k]
                if not toappend in allunitigkmers:
                    allunitigkmers[toappend] = currvindex
                    id_to_seq[currvindex] = toappend
                    currvindex += 1

        oldinvalid=invaliduni

        g = linesplit[1].rstrip()

        if g not in genomedict:
            genomedict[g]=genomeid
            genomeid +=1
            genomes.append(g)

        firstkmer = invaliduni[0:k]
        lastkmer = invaliduni[len(invaliduni)-k:]



        for i in range(len(g)-k+1):
            toappend = g[i:i+k]

            if not toappend in allunitigkmers:
                allunitigkmers[toappend] = currvindex
                id_to_seq[currvindex] = toappend

                #add first and last kmer of genome


                currvindex += 1

            vertex_to_genomeid[allunitigkmers[toappend]] = genomeid

        genomefirst[allunitigkmers[g[0:k]]] = genomeid
        genomelast[allunitigkmers[g[len(g)-k:len(g)]]] = genomeid


        firsts.append(allunitigkmers[firstkmer])
        lasts.append(allunitigkmers[lastkmer])

        line = reader.readline()

        # l_start = g.find(lastkmer)
        # f_start = g.find(firstkmer)

'''
startofblack=currvindex
with open(ref, 'r') as reader:
    #lobal currvindex
    line = reader.readline()
    if(line!=""):
        line=line.rstrip()
        for i in range(len(line)-k+1):
            toappend = line[i:i+k]
            if not toappend in allunitigkmers:
                allunitigkmers[toappend] = currvindex
                id_to_seq[currvindex] = toappend
                currvindex += 1
'''
# print(allunitigkmers)

startofblack=currvindex
cnt=0
with open("neikmer.txt", 'r') as reader:
    #lobal currvindex

    line = reader.readline()
    while(line!=""):

        toappend=line.rstrip()
        if not toappend in allunitigkmers:
            cnt+=1
            print(cnt)
            allunitigkmers[toappend] = currvindex
            id_to_seq[currvindex] = toappend
            currvindex += 1
        line = reader.readline()


'''
for kmomer, value in kmomerd.items():
    positions=list(find_all(refstr, kmomer))
    for p in positions:
        if p!=0 and p+k < len(refstr):
            toappend = refstr[p-1:p-1+k]
            if not toappend in allunitigkmers:
                allunitigkmers[toappend] = currvindex
                id_to_seq[currvindex] = toappend
                currvindex += 1
        if p+k < len(refstr):
            toappend = refstr[p:p+k]
            if not toappend in allunitigkmers:
                allunitigkmers[toappend] = currvindex
                id_to_seq[currvindex] = toappend
                currvindex += 1
'''



for kmer, index in allunitigkmers.items():
    suf=kmer[1:k]
    pre=kmer[0:k-1]
    if not suf in sdict:
        sdict[suf] = []
    sdict[suf].append(index)


    if not pre in pdict:
        pdict[pre] = []
    pdict[pre].append(index)

# print(sdict)
# print(pdict)
for i in range(0, currvindex):

    kmer2=id_to_seq[i]

    suff=kmer2[1:k]
    prep=kmer2[0:k-1]

    suflist=[]
    prelist=[]
    ins=False
    inp=False
    if suff in sdict:
        ins=True
        suflist=sdict[suff]
    if suff in pdict:
        inp=True
        prelist=pdict[suff]

    for j in suflist:
        for m in prelist:
            if not j in gr:
                gr[j] = []
            gr[j].append(m)
    if inp:
        del pdict[suff]
    if ins:
        del sdict[suff]

#print_graph()

# AT THIS POINT GRAPH IS Generated

for key, value in id_to_seq.items():
    if not key in gr:
        gr[key] = []
    indegree.append(0)
    outdegree.append(len(gr[key]))
    #print(key, outdegree[len(outdegree)-1])

for key, value in id_to_seq.items():
    for j in gr[key]:
        indegree[j] += 1

for key, value in id_to_seq.items():
    print(key, "in=",indegree[key], ",out=",outdegree[key])

out=open("oldgraph.gv", 'w')

outvertex=open("vertex.txt", 'w')

out.write("digraph d {\n")
for key, value in id_to_seq.items():
    print(key, value)

    outvertex.write("{0} {1}\n".format(key, value))

    # if key >= startofblack:
    #     out.write("{0} [label=\"{1}\", color=\"black\"]\n".format(key, id_to_seq[key]))
    # elif(key in firsts and key in lasts):
    #     out.write("{0} [label=\"{1}\", color=\"purple\"]\n".format(key, id_to_seq[key]))
    # elif(key in firsts and key not in lasts):
    #     out.write("{0} [label=\"{1}\", color=\"blue\"]\n".format(key, id_to_seq[key]))
    # elif(key in lasts and key not in firsts):
    #     out.write("{0} [label=\"{1}\", color=\"red\"]\n".format(key, id_to_seq[key]))
    # else:
    #     out.write("{0} [label=\"{1}\", color=\"green\"]\n".format(key, id_to_seq[key]))

    if key >= startofblack:
        out.write("{0} [label=\"{1}\", color=\"black\"]\n".format(key, key))
    elif(key in firsts and key in lasts):
        out.write("{0} [label=\"{1}\", color=\"purple\"]\n".format(key, key))
    elif(key in firsts and key not in lasts):
        out.write("{0} [label=\"{1}\", color=\"blue\"]\n".format(key, key))
    elif(key in lasts and key not in firsts):
        out.write("{0} [label=\"{1}\", color=\"red\"]\n".format(key, key))
    else:
        out.write("{0} [label=\"{1}\", color=\"green\"]\n".format(key, key))

outvertex.close()



for key, value in gr.items():
    for i in value:
        # out.write("{0} -> {1}[arrowhead=\"none\"]\n".format(key, i))
        out.write("{0} -> {1}[arrowhead=\"normal\"]\n".format(key, i))

out.write("}\n")

out.close()


## NOW COMPACTED ONE

#DO ADD GENOME FIRST AND LAST
for key, value in genomefirst.items():
    if indegree[key]==1:
        indegree[key] = 10
    if outdegree[key]==1:
        outdegree[key] = 10

for key, value in genomelast.items():
    if indegree[key]==1:
        indegree[key] = 10
    if outdegree[key]==1:
        outdegree[key] = 10


copycount={}
with open("copycount.txt", 'r') as reader:
    #lobal currvindex
    line = reader.readline()
    counter=0

    if line=='':
        print("done")

    while line != '':  # The EOF char is an empty string
        line=line.rstrip()

        copycount[counter] = int(line)
        counter += 1
        line = reader.readline()


def get_reverse_gr(graph):
    revgr=dict()
    for key, value in graph.items():
        for i in value:
            if i not in revgr:
                revgr[i] = []
            revgr[i].append(key)
    return revgr
#findunitig start
revgr=get_reverse_gr(gr)
unitigstartlist=[]
unitigendlist=[]
for key, value in id_to_seq.items():

    if key >= startofblack:
        issampled[key]=False
        isstart_of_inu[key] = False
        isend_of_inu[key] = False
    elif(key in firsts and key in lasts):
        issampled[key]=True
        isstart_of_inu[key] = True
        isend_of_inu[key] = True
        #out.write("{0} [label=\"{1}\", color=\"purple\"]\n".format(key, key))
    elif(key in firsts and key not in lasts):
        issampled[key]=True
        isstart_of_inu[key] = True
        isend_of_inu[key] = False
        #out.write("{0} [label=\"{1}\", color=\"blue\"]\n".format(key, key))
    elif(key in lasts and key not in firsts):
        issampled[key]=True
        isstart_of_inu[key] = False
        isend_of_inu[key] = True
        #out.write("{0} [label=\"{1}\", color=\"red\"]\n".format(key, key))
    else:
        issampled[key]=True
        isstart_of_inu[key] = False
        isend_of_inu[key] = False
        #out.write("{0} [label=\"{1}\", color=\"green\"]\n".format(key, key))

    if indegree[key] == 1:
        parent = revgr[key][0]
        if(outdegree[parent]>1):
            unitigstartlist.append(key)
    else:
        unitigstartlist.append(key)

    if outdegree[key] == 1:
        outparent = gr[key][0]
        if(indegree[outparent]>1):
            unitigendlist.append(key)
    else:
        unitigendlist.append(key)


shape={}
group_len={}

def dfs(graph, start, parent_of, visited, group_id, group_assign, group_end,shape, group_len):
    list1 = []
    list2 = []
    #parent_of = {}
    #visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            visited.add(vertex)
            #list1.append(parent_of.get(vertex, None))
            list2.append(vertex)




            if(vertex in unitigendlist):
                group_assign[vertex] = group_id
                print(vertex, id_to_seq[vertex],end='\n')
                group_end[group_id] =  vertex

                if(isstart_of_inu[vertex]):
                    shape[group_id] = "box"
                if(isend_of_inu[vertex]):
                    shape[group_id] = "diamond"

                group_len[group_id]=len(list2)
                return
            else:
                group_assign[vertex] = group_id

                if(isstart_of_inu[vertex]):
                    shape[group_id] = "box"
                if(isend_of_inu[vertex]):
                    shape[group_id] = "diamond"
                print(vertex, id_to_seq[vertex],end=' ')

            new_vertexes = set(graph[vertex]) - visited
            stack.extend(new_vertexes)
            # for i in new_vertexes:
            #     parent_of[i] = vertex
    #return parent_of




group_assign={}
visited=set()
parent_of={}
group_id=0
group_end={}
for key in unitigstartlist:
    if key not in visited:
        dfs(gr, key, parent_of, visited, group_id, group_assign, group_end, shape, group_len)
        group_id +=1
        #print(parent_of)

# print(parent_of)

compact_gr={}
for startvertex in unitigstartlist:
    grid = group_assign[startvertex]
    endvertex = group_end[grid]


    #for all in neigh of startvertex
    if startvertex not in revgr:
        revgr[startvertex] = []
    for inneigh in revgr[startvertex]:
        if group_assign[inneigh] not in compact_gr:
            compact_gr[group_assign[inneigh]] = set()
        compact_gr[group_assign[inneigh]].add(grid)


    if grid not in compact_gr:
        compact_gr[grid] = set()
    #for all out neigh of endvertex
    for outneigh in gr[endvertex]:
        compact_gr[grid].add(group_assign[outneigh])




'''
print compact GRAPH
'''
compout=open("graph.gv", 'w')
compout.write("digraph d {\n")
compout.write("node [colorscheme=SVG] \n")


iscolored={}
for key, value in compact_gr.items():
    #compout.write("{0} [label=\"{1}\", color=\"black\"]\n".format(key, key))
    #genomeid =


    endvertex = group_end[key]
    #copycount[endvertex] = 999999


    if endvertex not in vertex_to_genomeid:
        cc = 0
    else:
        cc=vertex_to_genomeid[endvertex] + 2

    shapp="ellipse"
    if group_assign[endvertex] in shape:
        shapp=shape[group_assign[endvertex]]


    if endvertex in genomefirst:
        compout.write("{0} [label=\"{1} ({2}){5}\", shape=\"{3}\", penwidth=5, style=\"dashed\", color=\"{4}\"]\n".format(key, endvertex, copycount[endvertex], shapp, colors[genomefirst[endvertex]+2],group_len[key]))
        iscolored[endvertex] = True
    if endvertex in genomelast:
        compout.write("{0} [label=\"{1} ({2}){5}\", shape=\"{3}\", penwidth=5, style=\"dotted\", color=\"{4}\"]\n".format(key, endvertex, copycount[endvertex], shapp, colors[genomelast[endvertex]+2],group_len[key]))
        iscolored[endvertex] = True
    if endvertex in genomefirst and endvertex in genomelast and len(genomes[genomefirst[endvertex]])!=k:
        compout.write("{0} [label=\"{1} ({2}){5}\", shape=\"{3}\", penwidth=5, style=\"diagonals\", color=\"{4}\"]\n".format(key, endvertex, copycount[endvertex], shapp, colors[0],group_len[key]))
        iscolored[endvertex] = True
    if endvertex not in genomefirst and endvertex not in genomelast:
        compout.write("{0} [label=\"{1} ({2}){5}\", shape=\"{3}\", penwidth=5, style=solid, color=\"{4}\"]\n".format(key, endvertex, copycount[endvertex], shapp, colors[cc], group_len[key]))
        iscolored[endvertex] = True

for key, value in compact_gr.items():
    for i in value:
        # out.write("{0} -> {1}[arrowhead=\"none\"]\n".format(key, i))
        compout.write("{0} -> {1}[arrowhead=\"normal\"]\n".format(key, i))
compout.write("}\n")
compout.close()





out = open("out.html","w")
out.write("<html>")
out.write("<body>")

with open("gtouch", 'r') as reader:
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

        assert (l_start==-1 or f_start==-1 or l_start <= f_start),"u_m should appear before u_0 in an invalid unitig!"

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
        out.write("<span style='color:{6};'>{0}</span><span style='color:red;'>{1}</span><span style='color:purple;'>{2}</span><span style='color:{6};'>{3}</span><span style='color:blue;'>{4}</span><span style='color:{6};'>{5}</span><br>".format(p1, redtext, purpletext, p2, bluetext, p3, "black"))
        #colors[vertex_to_genomeid[allunitigkmers[lastkmer]]]
#0+1+        2+      3   4       5
#p1+redtext+purpletext+p2+bluetext+p3




out.write("</body>")
out.write("</html>")

out.close()
