BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3
T=$4
mkdir -p $D/$K/$S/$T
cd $D/$K/$S/$T

#GET ONLY INVALIDS
cd $D/$K/$S/$T
#fmindex genomes.sset unid$K.sset #outputs: occsub issub
mkdir -p pseudo
cd pseudo

fmindex $D/ref.sset $D/$K/$S/$T/unid$K.sset

#Write only invalid unitigs
cat issub | grep 0 | cut -f2 -d" " > invalids
N_TOTUNI=$(wc -l $D/$K/$S/$T/unid$K.sset | cut -f1 -d" " )
N_INVALID=$(wc -l $D/$K/$S/$T/pseudo/invalids | cut -f1 -d" " )
N_CALG=$(wc -l $D/$K/$S/$T/genomes.sset | cut -f1 -d" ")
N_KMER=$(cat $D/$K/$S/$T/n_mer$K)

rm $D/$K/$S/$T/pseudo/gtouch
touch $D/$K/$S/$T/pseudo/gtouch
while read p; do
  #echo "$p"
  cat $D/$K/$S/$T/gtouch | grep $p >> $D/$K/$S/$T/pseudo/gtouch
done < $D/$K/$S/$T/pseudo/invalids
python $BASEDIR/gtouchsplit.py $D/$K/$S/$T/pseudo/gtouch $K

echo "$N_TOTUNI $N_INVALID $N_CALG $N_KMER" > report.txt
cat report.txt


cat invalids
