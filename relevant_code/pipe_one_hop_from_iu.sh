#NOW ACTUALLY TWO HOP
BASEDIR=$(dirname "$(realpath $0)")
F=$1
K=$2
#F="chr22lc"
#jellyfish count -m 18 -s 100M -t 10 ref.sset
cd $F
#cat gtouch | cut -f2 -d" " > invalid_genomes
python $BASEDIR/one_hop_from_iu.py invalids $K invalidnei1.txt
#python $BASEDIR/one_hop_from_iu.py invalid_genomes $K invalidnei1.txt
#jellyfish query mer_counts.jf $(cat invalidnei1.txt) | awk '$2 != "0"' | cut -f 1 -d " " > neikmer1.txt


rm neikmer1.txt 
touch neikmer1.txt
while IFS= read -r line
do
    jellyfish query mer_counts.jf $line | awk '$2 != "0"' | cut -f 1 -d " " >> neikmer1.txt
done < "invalidnei1.txt"


python $BASEDIR/one_hop_from_iu.py neikmer1.txt $K invalidnei2.txt
#jellyfish query mer_counts.jf $(cat invalidnei2.txt) | awk '$2 != "0"' | cut -f 1 -d " " > neikmer2.txt


rm neikmer2.txt 
touch neikmer2.txt
while IFS= read -r line
do
    jellyfish query mer_counts.jf $line | awk '$2 != "0"' | cut -f 1 -d " " >> neikmer2.txt
done < "invalidnei2.txt"


cat neikmer1.txt neikmer2.txt | uniq > neikmer.txt



#jellyfish query mer_counts.jf $(cat invalidnei_twohop.txt) | awk '$2 != "0"' | cut -f 1 -d " " > nei2kmer.txt

#jellyfish query mer_counts.jf $(cat invalidnei.txt) | awk '$2 != "0"' | cut -f 1 -d " " > nei2kmer.txt
#cat nei2kmer.txt | uniq > neikmer.txt


#jellyfish query mer_counts.jf $(cat vertex.txt | cut -f2 -d" ") | cut -f2 -d" " > copycount.txt
#cat chr22lc/vertex.txt | awk '$1 != "11240"'
