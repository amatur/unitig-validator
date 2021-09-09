D=$1
K=$2
cd $D
cat ref.sset | awk '{print ">contig\n" $0}' > ref.fa
jellyfish count -m $K -s 100M -t 10 ref.fa

