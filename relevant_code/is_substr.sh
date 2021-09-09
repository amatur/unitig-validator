# usage ./sufar_test.sh where_to_search what_to_search

SAFILE="tmp_safile"
FAFILE=$1

OUTFILE=$3
rm -rf $OUTFILE

SASEARCH=~/w/AvxWindowFmIndex/libdivsufsort/build/examples/sasearch
MKSARY=~/w/AvxWindowFmIndex/libdivsufsort/build/examples/mksary

$MKSARY $FAFILE $SAFILE

searchInSA(){
	out=$($SASEARCH $1 $FAFILE $SAFILE) 
	if [ -z "$out" ] 
	then 
        	echo "0" >> $OUTFILE
	else 
        	echo "1" >> $OUTFILE
	fi 
}


while IFS= read -r line; do
    searchInSA $line
done < $2
