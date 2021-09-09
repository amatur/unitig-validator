BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3
mkdir -p $D/$K/c/$S
cd $D/$K/c/$S/

#GET ONLY INVALIDS
cd $D/$K/c/$S/

#Write only invalid unitigs
cat issub | grep 0 | cut -f2 -d" " > invalids
N_TOTUNI=$(wc -l unid$K.sset | cut -f1 -d" " )
N_INVALID=$(wc -l invalids | cut -f1 -d" " )
N_CALG=$(wc -l segfile.sset | cut -f1 -d" ")
N_KMER=$(cat n_mer$K)

echo "N_TOTUNI PSEUDO_INVALID CALG N_KMER "
echo "$N_TOTUNI $N_INVALID $N_CALG $N_KMER" > report.txt
cat report.txt


U=$D/$K/c/$S/pseudo/invalids

rm result
touch result

rm gtouch
touch gtouch
rm occ_*


while read INVALID; do
        python $BASEDIR/sub_count.py $D/$K/c/$S/segfile.sset $K $INVALID
        tot1=$(cat occ_1 | grep 1 | wc -l)
        tot2=$(cat occ_2 | grep 1 | wc -l)
        tot3=$(cat occ_3 | grep 1 | wc -l)
        tot4=$(cat occ_4 | grep 1 | wc -l)
        echo "$tot1 $tot2 $tot3 $tot4" >> result
done < $U

echo "gtouch ready in $D/$K/c/$S/pseudo/gtouch"
#python $BASEDIR/gtouchsplit.py $D/$K/$S/$T/gtouch $K

#awk -F' ' '{sum+=$4;} END{print sum;}' result

echo "Num of truly invalid:  $(cat $D/$K/c/$S/pseudo/gtouch | wc -l | cut -f1 -d' ')"
