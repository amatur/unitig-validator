K=$1
cat ref.sset | awk '{print ">contig\n" $0}' > ref.fa
jellyfish count -m $K -s 100M -t 10 ref.fa
