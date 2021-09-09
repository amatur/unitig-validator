BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3
mkdir -p $D/$K/c/$S/
cd $D/$K/c/$S/

mkdir -p pseudo
cd pseudo

fmindex $D/ref.sset $D/$K/c/$S/unid$K.sset

#Write only invalid unitigs
cat issub | grep 0 | cut -f2 -d" " > invalids
N_TOTUNI=$(wc -l $D/$K/c/$S/unid$K.sset | cut -f1 -d" " )
N_INVALID=$(wc -l $D/$K/c/$S/pseudo/invalids | cut -f1 -d" " )
N_KMER=$(cat $D/$K/c/$S/n_mer$K)

rm $D/$K/c/$S/pseudo/gtouch
touch $D/$K/c/$S/pseudo/gtouch
while read p; do
  cat $D/$K/c/$S/gtouch | grep $p >> $D/$K/c/$S/pseudo/gtouch
done < $D/$K/c/$S/pseudo/invalids
#python $BASEDIR/gtouchsplit.py $D/$K/c/$S/pseudo/gtouch $K

echo "$N_TOTUNI $N_INVALID $N_KMER" > report.txt
cat report.txt


#cat invalids
