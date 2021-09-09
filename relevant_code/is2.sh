# usage ./sufar_test.sh where_to_search what_to_search

SAFILE="tmp_safile"
FAFILE=$1

OUTFILE=$3
rm -rf $OUTFILE

SASEARCH=~/w/AvxWindowFmIndex/libdivsufsort/build/examples/sasearch
MKSARY=~/w/AvxWindowFmIndex/libdivsufsort/build/examples/mksary


~/s/test_ddbd/unitig-validator/aedes/sdsl-lite/examples/fmindex $FAFILE $2
echo "output in issub"
