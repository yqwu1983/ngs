#!/bin/bash
name='Euglena_genome'
input='/home/anna/bioinformatics/euglena/Euglena_gracilis_genome_V1.fasta'
lineage='/home/anna/bioinformatics/bioprograms/busco_lineages/eukaryota'
# python BUSCO_v1.1b1.py -o $name -in $input -l $lineage -m genome -f

python BUSCO_v1.1b1.py -o Euglena_genome -in /home/anna/bioinformatics/euglena/Euglena_gracilis_genome_V1.fasta -l /home/anna/bioinformatics/bioprograms/busco_lineages/eukaryota -m genome -f
python BUSCO_v1.1b1.py -o Euglena_proteome -in /home/anna/bioinformatics/euglena/E_gracilis_transcriptome_final.PROTEINS.fasta -l /home/anna/bioinformatics/bioprograms/busco_lineages/eukaryota -m OGS