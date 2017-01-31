#!/bin/bash
outdir="/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/pandoraea_prokka"
genome="/home/anna/Dropbox/PhD/bioinformatics/genomes/trypanosomatids/novymonas/pandoraea_final.fasta"
prokka --cpus 4 --centre XXX --kingdom Bacteria  --gram neg --addgenes --genus "Pandoraea" --force --outdir $outdir $genome
