BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3
mkdir -p $D/$K/c/$S
cd $D/$K/c/$S

#s gap len
#T gap freq
python $BASEDIR/simu_read_rand.py $D/ref.sset $D/$K/c/$S/ref_read.sset $S $K

$BASEDIR/sset_to_fa.sh $D/$K/c/$S/ref_read.sset > $D/$K/c/$S/ref_read.fa
$BASEDIR/directed_unitigs.sh $D/$K/c/$S/ref_read.fa $K

#GET ONLY INVALIDS
cd $D/$K/c/$S/
rm -rf segfile.sset.fm9
fmindex segfile.sset unid$K.sset #outputs: occsub issub

echo "reporting: "
cat issub | grep 0 | cut -f2 -d" " > invalids
N_TOTUNI=$(wc -l unid$K.sset | cut -f1 -d" " )
N_INVALID=$(wc -l invalids | cut -f1 -d" " )
N_KMER=$(cat n_mer$K)


mkdir -p pseudo
cd pseudo
#rm -rf  ref.sset.fm9
fmindex ../../../../ref.sset ../invalids  #outputs: occsub issub
cat issub | grep 0 | cut -f2 -d" " > invalids
N_TINVALID=$(wc -l invalids | cut -f1 -d" " )


echo "tot_uni invalid true_invalid n_kmer"
echo "$N_TOTUNI $N_INVALID $N_TINVALID $N_KMER" > report.txt
cat report.txt

#GET TRULY INVALID UNITIGS





### ALL 
#$BASEDIR/pipe_pseudo_read.sh $D $K $S
