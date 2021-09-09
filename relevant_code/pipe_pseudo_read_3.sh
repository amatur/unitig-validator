BASEDIR=$(dirname "$(realpath $0)")
#echo "$BASEDIR"
D=$(realpath $1)
K=$2
S=$3


cd $D/$K/c/$S/pseudo
rm gtouch
touch gtouch

while read INVALID; do
        python $BASEDIR/sub_count.py $D/$K/c/$S/segfile.sset $K $INVALID
done < invalids

python $BASEDIR/gtouchsplit.py $D/$K/c/$S/pseudo/gtouch $K


