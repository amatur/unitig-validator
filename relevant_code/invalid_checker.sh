F=$1
K=$2
SS=$(basename $F .fa)
S=$(echo "$SS.sset")
RP=$(realpath $0)
RD=$(dirname $RP) 
$RD/directed_unitigs.sh $F $K
$RD/is_substr.sh $S dir_uni$K.sset issub_$K.txt

