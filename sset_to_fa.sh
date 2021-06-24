#BAZE=$(basename $1 .sset)
cat $1 | awk '{print ">contig\n" $0}'
