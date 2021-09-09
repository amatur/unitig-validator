#NOW ACTUALLY TWO HOP
BASEDIR=$(dirname "$(realpath $0)")
F=$1
K=$2
#F="chr22lc"
#jellyfish count -m 18 -s 100M -t 10 ref.sset
cd $F
#cat gtouch | cut -f2 -d" " > invalid_genomes
#python $BASEDIR/one_hop_from_iu.py invalids $K invalidnei1.txt
python $BASEDIR/one_hop_from_iu.py invalid_genomes $K invalidnei1.txt
#jellyfish query mer_counts.jf $(cat invalidnei1.txt)  | awk '$2 != "0"' | cut -f 1 -d " " > neikmer1.txt

rm neikmer1.txt
touch neikmer1.txt
linen=$(wc -l invalidnei1.txt | cut -f1 -d" " )
files=$(cat invalidnei1.txt | tr '\n' ' ')
echo $linen
#while IFS= read -r line
#do
#   look -b $line sortcount  >> neikmer1.txt
#   # | awk '$2 != "0"' | cut -f 1 -d " " >> neikmer1.txt
#done < invalidnei1.txt

for (( i=1; i<=$linen; i+=10000 )); do
   j=$((i+100-1))
	echo "$i $j"
   query=$(awk -v i=$i -v j=$j 'NR>=i&&NR<=j' invalidnei1.txt )
   echo $query | jellyfish query -i mer_counts.jf >> neikmer1.txt
# | awk '$2 != "0"' >> neikmer1.txt
# | cut -f 1 -d " " >> neikmer1.txt
done
#wc -l neikmer1.txt

cat invalidnei1.txt | jellyfish query -i mer_counts.jf > neikmer1.tmp
paste -d " " invalidnei1.txt neikmer1.tmp | awk '$2 != "0"' | cut -f 1 -d " " > neikmer1.txt 
rm neikmer1.tmp


#rm neikmer1.txt 
#touch neikmer1.txt
#while IFS= read -r line
#do
#    jellyfish query mer_counts.jf $line | awk '$2 != "0"' | cut -f 1 -d " " >> neikmer1.txt
#done

#cat neikmer1.txt | uniq > neikmer.txt



#jellyfish query mer_counts.jf $(cat invalidnei_twohop.txt) | awk '$2 != "0"' | cut -f 1 -d " " > nei2kmer.txt

#jellyfish query mer_counts.jf $(cat invalidnei.txt) | awk '$2 != "0"' | cut -f 1 -d " " > nei2kmer.txt
#cat nei2kmer.txt | uniq > neikmer.txt


#jellyfish query mer_counts.jf $(cat vertex.txt | cut -f2 -d" ") | cut -f2 -d" " > copycount.txt
#cat chr22lc/vertex.txt | awk '$1 != "11240"'
