#F=$1
#K=$2

U=invalids
K=25

rm result
touch result
while read INVALID; do
	python sub_count.py testnon.sset $K $INVALID
	tot1=$(cat occ_1 | grep 1 | wc -l)
	tot2=$(cat occ_2 | grep 1 | wc -l)
	tot3=$(cat occ_3 | grep 1 | wc -l)
	tot4=$(cat occ_4 | grep 1 | wc -l)
	echo "$tot1 $tot2 $tot3 $tot4" >> result
done < $U

