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

#Write only invalid unitigs
cat issub | grep 0 | cut -f2 -d" " > invalids
N_TOTUNI=$(wc -l unid$K.sset | cut -f1 -d" " )
N_INVALID=$(wc -l invalids | cut -f1 -d" " )

echo "$N_TOTUNI $N_INVALID" > report.txt
cat report.txt


U=invalids

rm result
touch result

rm gtouch
touch gtouch

while read INVALID; do
        python $BASEDIR/sub_count.py genomes.sset $K $INVALID
        tot1=$(cat occ_1 | grep 1 | wc -l)
        tot2=$(cat occ_2 | grep 1 | wc -l)
        tot3=$(cat occ_3 | grep 1 | wc -l)
        tot4=$(cat occ_4 | grep 1 | wc -l)
        echo "$tot1 $tot2 $tot3 $tot4" >> result
done < $U

