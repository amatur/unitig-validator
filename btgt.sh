D=$1
K=$2
C=$3
#O=$4
CODE_DIR=$(dirname "$(realpath $0)")

D=$(realpath $1)
#OR=$(realpath $O)
#mkdir -p $OR
#cd $OR
#cp $D/$K/c/$C/segfile.sset .
#cp $D/$K/c/$C/pseudo/invalids iutrue.sset 

IUT="$D/$K/c/$C/pseudo/invalids"
IUT_KMERS="iumers_$K.sset"
IUT_KMERS_FA="iumers_$K.fa"
SEG="$D/$K/c/$C/segfile.sset"
SEG_FA="$D/$K/c/$C/segfile.fa"
JF_FILE="$D/$K/mer_counts.jf"

python $CODE_DIR/all_kmer_from_iu.py $IUT  $K $IUT_KMERS 
sset_to_fa.sh $IUT_KMERS > $IUT_KMERS_FA

cd $D/$K
if [[ ! -f "$JF_FILE" ]]; then
	if [[ ! -f "$D/ref.fa" ]]; then
		sset_to_fa.sh $D/ref.sset > $D/ref.fa
	fi
	jellyfish count -m $K -s 100M -t 10 $D/ref.fa
fi


cd $D/$K/c/$C/

#SEGFILE_INDEX
if [[ ! -f "$SEG" ]]; then
	echo "$SEG" is an invalid file.
	exit 2
fi

sset_to_fa.sh $SEG > $SEG_FA
if [[ ! -f seg_iutkmer.sam ]]; then
	~/w/bowtie/bowtie-build -p -f $SEG_FA segindex
fi
NUM_STRING=$(cat $SEG | wc -l)

~/w/bowtie/bowtie -s -a -k $NUM_STRING -v 0 segindex -f $IUT_KMERS_FA  --un unaligned_kmers.fa --al aligned_kmers.fa --norc > seg_iutkmer.sam
cat seg_iutkmer.sam | cut -f1,3 > pair
python $CODE_DIR/just_gtouch.py $IUT_KMERS_FA $IUT $SEG_FA  pair
cat gtouch_bt | sort | uniq  > gtouch_true
python $CODE_DIR/dbgofinvalid.py $K gtouch_true $JF_FILE
echo "Final figure in "
echo "$(realpath dbg_nomis.svg)"
