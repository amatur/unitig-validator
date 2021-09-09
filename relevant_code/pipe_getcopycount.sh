#NOW ACTUALLY TWO HOP
BASEDIR=$(dirname "$(realpath $0)")
F=$1
K=$2
cd $F

#sset_to_fa.sh ref.sset > ref.fa
jellyfish count -m $K -s 100M -t 10 ref.fa
#jellyfish dump -c mer_counts.jf > mer_counts_dumps.fa


jellyfish query mer_counts.jf $(cat vertex.txt | cut -f2 -d" ") | cut -f2 -d" " > copycount.txt
