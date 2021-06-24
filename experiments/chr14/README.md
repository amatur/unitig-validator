# Pipeline to get invalid unitigs from chr14
Scripts to check if a unitig is substring of input string(s)

## nremover.py
Sample command:
`python nremover.py`


### Prepare input: set of genomes

Step 1: Download FASTA from SRA
`fastq-dump --fasta SRR067577`

Step 2:
Trim new line (Multi line fasta to single line)   
`cat SRR067577.fasta | awk '/^>/ {printf("\n%s\n",$0);next; } { printf("%s",$0);}  END {printf("\n");}' | tail -n +2 > single.fa`

Step 3:
Convert fa to sset
`cat single.fa | sed '/^>/d' > single.sset`

Step 4:
Split strings across N in sset
`python ../nremover.py single.sset > nsplit.sset`

Step 5:
Subsetting: keep only genomes with at least k length.
`cat nsplit.sset | awk 'length($0)>29' > gr29.sset`

Step 6:
Subsetting: keep first 50k genomes.
`cat gr29.sset | head -n 50000 > genomes.sset`

Step 7:
Convert sset to fa
`../sset_to_fa.sh genomes.sset > genomes.fa`

Step 8:
Run directed unitigs maker [Input: Fasta file, single line, Output: unid29.fa]
`./directed_unitigs genomes.fa 29`

### Run experiments
TODO
