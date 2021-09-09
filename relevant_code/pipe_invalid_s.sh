BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3
T=$4
mkdir -p $D/$K/$S/$T
cd $D/$K/$S/$T

#s gap len
#T gap freq
#cat $D/gr29.sset | head -n $S > $D/$K/$S/genomes.sset

python $BASEDIR/simu_rand.py $D/ref.sset $D/$K/$S/$T/refn.sset $S $T
python $BASEDIR/nremover.py  $D/$K/$S/$T/refn.sset > $D/$K/$S/$T/nsplit.sset
cat $D/$K/$S/$T/nsplit.sset | awk -v var=$K 'length($0)>var' | head -n 50000 > $D/$K/$S/$T/genomes.sset

$BASEDIR/sset_to_fa.sh $D/$K/$S/$T/genomes.sset > $D/$K/$S/$T/genomes.fa
$BASEDIR/directed_unitigs.sh $D/$K/$S/$T/genomes.fa $K

#GET ONLY INVALIDS
cd $D/$K/$S/$T
rm genomes.sset.fm9
fmindex genomes.sset unid$K.sset #outputs: occsub issub

echo "reporting:"
$BASEDIR/pipe_reporter_s.sh $D $K $S $T

$BASEDIR/pipe_pseudo.sh $D $K $S $T 
