F=$1
# K=31

for K in $2
do
   
	### FOR DOUBLE DIRECTED
	jellyfish count -m $K -s 100M -t 10 $F
	jellyfish dump -c mer_counts.jf > mer_counts_dumps.fa


	#cat kmersascii.txt | cut -f 1 -d"" \; > fwd_kmer.txt
	cat mer_counts_dumps.fa | cut -f 1 -d" " |  awk '{print $0" 1"}'  > dbg_fwd.txt
	cat dbg_fwd.txt | tr ACGTacgt TGCAtgca | rev > dbg_bwd.txt

	cat dbg_fwd.txt dbg_bwd.txt | uniq > dbg_both.txt
	echo "$(cat dbg_both.txt | wc -l)" > n_mer$K 


	malfoybcalm  dbg_fwd.txt dbg$K.txt 2
	# BCALM/bcalm  mer_counts_dumps.fa dd.unitigs 2

	cat dbg$K.txt | tr a A | tr c C | tr g G | tr t T | tr -d \; > unid$K.sset
	
done



rm mer_counts.jf 
rm mer_counts_dumps.fa 
rm largest_bucket.dot 
rm dbg_fwd.txt 
rm dbg_bwd.txt
rm dbg_both.txt  
rm dbg$K.txt 

