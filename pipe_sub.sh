BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3
mkdir -p $D/$K/$S
cd $D/$K/$S

#GET ONLY INVALIDS
cd $D/$K/$S
#fmindex genomes.sset unid$K.sset #outputs: occsub issub


U=invalid_sub

rm result_sub
touch result_sub

rm gtouch_sub
touch gtouch_sub

while read INVALID; do
        python $BASEDIR/sub_count.py genomes.sset $K $INVALID
        tot1=$(cat occ_1 | grep 1 | wc -l)
        tot2=$(cat occ_2 | grep 1 | wc -l)
        tot3=$(cat occ_3 | grep 1 | wc -l)
        tot4=$(cat occ_4 | grep 1 | wc -l)
        echo "$tot1 $tot2 $tot3 $tot4" >> result_sub
done < $U

