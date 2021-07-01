
countA=$(cat $1 | tr -cd 'A' | wc -c)
countC=$(cat $1 | tr -cd 'C' | wc -c)
countG=$(cat $1 | tr -cd 'G' | wc -c)
countT=$(cat $1 | tr -cd 'T' | wc -c)
sum=$((countA + countC + countG + countT))
echo "$countA $countT $countG $countC"
echo "$sum"

