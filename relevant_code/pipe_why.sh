BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3
mkdir -p $D/$K/c/$S
cd $D/$K/c/$S

#s gap len
#T gap freq
#cat $D/gr29.sset | head -n $S > $D/$K/$S/genomes.sset


#GET ONLY INVALIDS
cd $D/$K/c/$S/
rm segfile.sset.fm9
fmindex segfile.sset unid$K.sset #outputs: occsub issub

echo "reporting: non true"
cat issub | grep 0 | cut -f2 -d" " > invalids
N_TOTUNI=$(wc -l unid$K.sset | cut -f1 -d" " )
N_INVALID=$(wc -l invalids | cut -f1 -d" " )
N_KMER=$(cat n_mer$K)

echo "$N_TOTUNI $N_INVALID $N_KMER" > report.txt
cat report.txt



$BASEDIR/pipe_pseudo_read.sh $D $K $S
