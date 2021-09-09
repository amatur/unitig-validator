BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3
mkdir -p $D/$K/$S
cd $D/$K/$S

cat $D/gr29.sset | head -n $S > $D/$K/$S/genomes.sset
$BASEDIR/sset_to_fa.sh $D/$K/$S/genomes.sset > $D/$K/$S/genomes.fa
$BASEDIR/directed_unitigs.sh genomes.fa $K

#GET ONLY INVALIDS
cd $D/$K/$S
fmindex genomes.sset unid$K.sset #outputs: occsub issub

$BASEDIR/pipe_reporter.sh $D $K $S
