strandedBamImport <- function (file, selection) {
  if (!file.exists(paste(file, "bai", sep = ".")))
    stop("Unable to find index for BAM file '", file, "'. You can
         build an index using the following command:\n\t",
         "library(Rsamtools)\n\tindexBam(\"", file, "\")")
  sinfo <- scanBamHeader(file)[[1]]
  res <- if (!as.character(seqnames(selection)[1]) %in%
               names(sinfo$targets)) {
    mcols(selection) <- DataFrame(score = 0)
    selection
  }else {
    param <- ScanBamParam(what = c("pos", "qwidth", "strand"),
                          which = selection, flag =
                            scanBamFlag(isUnmappedQuery = FALSE))
    x <- scanBam(file, param = param)[[1]]
    gr <- GRanges(strand=x[["strand"]], ranges=IRanges(x[["pos"]],
                                                       width = x[["qwidth"]]), seqnames=seqnames(selection)[1])
    grs <- split(gr, strand(gr))
    cov <- lapply(grs[c("+", "-")], function(y) coverage(ranges(y),
                                                         width=end(selection)))
    pos <- sort(unique(unlist(lapply(cov, function(y) c(start(y),
                                                        end(y))))))
    if(length(pos)==0){
      mcols(selection) <- DataFrame(plus=0, minus=0)
      selection
    }else{
      GRanges(seqnames = seqnames(selection)[1],
              ranges=IRanges(start=head(pos, -1), end=tail(pos, -1)),
              plus=as.numeric(cov[["+"]][head(pos, -1)]),
              minus=-as.numeric(cov[["-"]][head(pos, -1)]))
    }
  }
  return(res)
}

library(Gviz)
options(ucscChromosomeNames=FALSE)

#library(biomaRt)
#mart = useMart("ensembl",dataset="rnorvegicus_gene_ensembl")

myChr = 'gi|45774915|gb|AY543070.1|'
myStart = 10000
myEnd = 20000000
genome = '45774915'

# First create track with gene model:
#biomTrack = BiomartGeneRegionTrack(genome=genome, biomart=mart, chromosome=myChr, start=myStart, end=myEnd,showId=F, geneSymbols=F, rotate.title=TRUE, col.line=NULL, col="orange", fill="orange",filters=list(biotype="protein_coding"),collapseTranscripts=FALSE)

# now create data track using new import function:
#bamFile = "path/to/bam/file"
bamFile = "/home/anna/bioinformatics/outdirs/T5adapt_ACTTGA_L001_R1_001/bowtie2_out_t5/alignment.sorted.bam"
dataTrack = DataTrack(bamFile, chromosome=myChr, importFunction=strandedBamImport, stream=TRUE, legend=TRUE, col=c("cornflowerblue","purple"), groups=c("Forward","Reverse"), name="Coverage")

# now plot tracks:
plotTracks(dataTrack, from = myStart, to = myEnd, type="hist", col.histogram=NA, cex.title=1, cex.axis=1, title.width=1.2)
