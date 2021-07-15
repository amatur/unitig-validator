BASEDIR=$(dirname "$(realpath $0)")
F=$1
K=$2
#F="chr22lc"
#jellyfish count -m 18 -s 100M -t 10 ref.sset
cd $F
python $BASEDIR/one_hop_from_iu.py invalids $K
jellyfish query mer_counts.jf $(cat invalidnei.txt) | awk '$2 != "0"' | cut -f 1 -d " " > neikmer.txt
jellyfish query mer_counts.jf $(cat vertex.txt | cut -f2 -d" ") | cut -f2 -d" " > copycount.txt
#cat chr22lc/vertex.txt | awk '$1 != "11240"'
