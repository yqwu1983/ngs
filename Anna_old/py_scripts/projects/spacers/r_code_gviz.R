# A function to extract reads from a stranded RNA-seq BAM file.  Intended to be used as a custom importFunction 
# in the DataTrack constructor of Bioconductor's Gviz package. With properly stranded data this allows the plotting 
# of coverage tracks from each strand of the genome.
#
# NOTE: this is written for libraries with forward/top strand pairs in the orientation of F2R1 and reverse/bottom 
# strand pairs as F1R2. Yo will need to switch the scanBamFlag's around if your library is in the other direction.
#
# 6 Nov 2014 - bensidders at gmail dot com

strandedBamImport = function (file, selection) {
	
	require(Rsamtools)
	
	if (!file.exists(paste(file, "bai", sep = "."))) {
        stop("Unable to find index")
	}
    
	# get pos strand pairs (F2R1):
	param_f2 = ScanBamParam(what = c("pos", "qwidth", "strand"), which = selection, flag = scanBamFlag(isUnmappedQuery = FALSE, isProperPair = TRUE, isFirstMateRead = FALSE, isMinusStrand = FALSE))
	x_f2 = scanBam(file, param = param_f2)[[1]]
	gr_f2 = GRanges(strand=x_f2[["strand"]], ranges=IRanges(x_f2[["pos"]], width = x_f2[["qwidth"]]), seqnames=seqnames(selection)[1])

	param_r1 = ScanBamParam(what = c("pos", "qwidth", "strand"), which = selection, flag = scanBamFlag(isUnmappedQuery = FALSE, isProperPair = TRUE, isFirstMateRead = TRUE, isMinusStrand = TRUE))
	x_r1 = scanBam(file, param = param_r1)[[1]]
	gr_r1 = GRanges(strand=x_r1[["strand"]], ranges=IRanges(x_r1[["pos"]], width = x_r1[["qwidth"]]), seqnames=seqnames(selection)[1])

	gr_f2r1 = c(gr_f2,gr_r1)

	# get rev strand reads (F1R2):
	param_f1 = ScanBamParam(what = c("pos", "qwidth", "strand"), which = selection, flag = scanBamFlag(isUnmappedQuery = FALSE, isProperPair = TRUE, isFirstMateRead = TRUE, isMinusStrand = FALSE))
	x_f1 = scanBam(file, param = param_f1)[[1]]
	gr_f1 = GRanges(strand=x_f1[["strand"]], ranges=IRanges(x_f1[["pos"]], width = x_f1[["qwidth"]]), seqnames=seqnames(selection)[1])

	param_r2 = ScanBamParam(what = c("pos", "qwidth", "strand"), which = selection, flag = scanBamFlag(isUnmappedQuery = FALSE, isProperPair = TRUE, isFirstMateRead = FALSE, isMinusStrand = TRUE))
	x_r2 = scanBam(file, param = param_r2)[[1]]
	gr_r2 = GRanges(strand=x_r2[["strand"]], ranges=IRanges(x_r2[["pos"]], width = x_r2[["qwidth"]]), seqnames=seqnames(selection)[1])

	gr_f1r2 = c(gr_f1,gr_r2)


	# calc coverage on both strands:
	cov_list = list("Forward" = coverage(ranges(gr_f2r1), width=end(selection)), "Reverse" = coverage(ranges(gr_f1r2), width=end(selection)))
	pos = sort(unique(unlist(lapply(cov_list, function(y) c(start(y), end(y))))))

	# build final GR
	stranded_cov_gr = GRanges(seqnames = seqnames(selection)[1], ranges=IRanges(start=head(pos, -1), end=tail(pos, -1)),
		plus=as.numeric(cov_list[["Forward"]][head(pos, -1)]),
		minus=-as.numeric(cov_list[["Reverse"]][head(pos, -1)]))
	
	return(stranded_cov_gr)
}
