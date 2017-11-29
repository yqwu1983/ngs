#!/bin/bash
for file in *.fastq;
do tar czvf "${file}".tar.gz "${file}" && rm "${file}"; done
