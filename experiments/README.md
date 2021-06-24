# unitig-validator
Scripts to check if a unitig is substring of input string(s)

## nremover.py
Sample command:
`python nremover.py`


Prepare input: set of genomes

Step 1: Download FASTA from SRA
`fastq-dump --fasta SRR390728`

Step 2:
Trim new line (Multi line fasta to single line)   
`cat SRR390728.fasta | awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' | tail -n +2 > SRR390728.fa`

Step 3:
Convert fa to sset
`cat SRR390728.fa | sed '/^>/d' > SRR390728.sset`

Step 4:
Split all n in sset
`python nremover.py SRR390728.sset > SRR390728_nsplit.sset`

Step 5:
Get min length
`MINLEN=$(cat SRR390728_nsplit.sset | awk '{print length}' | sort -n | head -n1)`

Step 6:
Convert sset to fa
`cat SRR390728_nsplit.sset | awk '{print ">contig\n" $0}' > SRR390728_nsplit.fa`

Step 7:
Get all non-canonical fwd kmers
`./fwd_kmers SRR390728_nsplit.fa > SRR390728_nsplit_fwdkmers`

Step 8:
Run directed unitigs maker [Input: File where each line is a k-mer]
`./directed_unitigs SRR390728_nsplit_fwdkmers > SRR390728_nsplit_fwdkmers_diuni.fa`


Step 9:
Validate
For each string in sset, report only invalid unitigs


Step 10:
Get only invalid unitigs
0 ones


Step 11:
Check if
