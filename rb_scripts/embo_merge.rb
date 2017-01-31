#!/usr/bin/ruby
merge_list = [
    { forward: '1F-cul13_GAPDHG_premix.seq.clipped', reverse: '1R-cul13_GAPDHG_premix.seq.clipped' },
    { forward: '2F-cul13ova_GAPDHG_premix.seq.clipped', reverse: '2R-cul13ova_GAPDHG_premix.seq.clipped' },
    { forward: '3F-Fi-14_semi_GAPDHG_premix.seq.clipped', reverse: '3R-Fi-14_semi_GAPDHG_premix.seq.clipped' },
    { forward: '4F-Fi-14p23_GAPDHG_premix.seq.clipped', reverse: '4R-Fi-14p23_GAPDHG_premix.seq.clipped' },
    { forward: '5F-CC37A_GAPDHG_premix.seq.clipped', reverse: '5R-CC37A_GAPDHG_premix.seq.clipped' },
    { forward: '6F-CC49A_GAPDHG_premix.seq.clipped', reverse: '6R-CC49A_GAPDHG_premix.seq.clipped' },
    { forward: '6F-CC49A_GAPDHG_premix#2.seq.clipped', reverse: '6R-CC49A_GAPDHG_premix#2.seq.clipped' },
    { forward: '7F-cul13_SSU_premix.seq.clipped', reverse: '7R-cul13_SSU_premix.seq.clipped' },
    { forward: '8F-cul13ova_SSU_premix.seq.clipped', reverse: '8R-cul13ova_SSU_premix.seq.clipped' },
    { forward: '9F-Fi-14_semi_SSU_premix.seq.clipped', reverse: '9R-Fi-14_semi_SSU_premix.seq.clipped' },
    { forward: '9F-P57p27_762763_premix.seq.clipped', reverse: '9R-P57p27_762763_premix.seq.clipped' },
    { forward: '10F-Fi-14p23_SSU_premix.seq.clipped', reverse: '10R-Fi-14p23_SSU_premix.seq.clipped' },
    { forward: '10F-P57p43_762763_premix.seq.clipped', reverse: '10R-P57p43_762763_premix.seq.clipped' },
    { forward: '11F-CC37A_SSU_premix.seq.clipped', reverse: '11R-CC37A_SSU_premix.seq.clipped' },
    { forward: '11F-Fi-14_semi_SSU_premix.seq.clipped', reverse: '11R-Fi-14_semi_SSU_premix.seq.clipped' },
    { forward: '12F-CC49A_SSU_premix.seq.clipped', reverse: '12R-CC49A_SSU_premix.seq.clipped' },
    { forward: '12F-CC49A_SSU_premix.seq2.clipped', reverse: '12R-CC49A_SSU_premix.seq2.clipped' },
    { forward: '13F-P57p16_SSU_premix.seq.clipped', reverse: '13R-P57p16_SSU_premix.seq.clipped' },
    { forward: '13F-P57p27_SSU_premix.seq.clipped', reverse: '13R-P57p27_SSU_premix.seq.clipped' },
    { forward: '14F-P57p35_SSU_premix.seq.clipped', reverse: '14R-P57p35_SSU_premix.seq.clipped' },
    { forward: '14F-P57p43_SSU_premix.seq.clipped', reverse: '14R-P57p43_SSU_premix.seq.clipped' },
    { forward: '15F-cul13ova_GAPDHM_premix.seq.clipped', reverse: '15R-cul13ova_GAPDHM_premix.seq.clipped' },
    { forward: '16F-Fi-14_semi_GAPDHM_premix.seq.clipped', reverse: '16R-Fi-14_semi_GAPDHM_premix.seq.clipped' },
    { forward: '17F-Fi-14p23_GAPDHM_premix.seq.clipped', reverse: '17R-Fi-14p23_GAPDHM_premix.seq.clipped' },
    { forward: '18F-CC37A_GAPDHM_premix.seq.clipped', reverse: '18R-CC37A_GAPDHM_premix.seq.clipped' },
    { forward: '19F-CC49A_GAPDHM_premix.seq.clipped', reverse: '19R-CC49A_GAPDHM_premix.seq.clipped' },
    { forward: '20F-cul13_762763_premix.seq.clipped', reverse: '20R-cul13_762763_premix.seq.clipped' },
    { forward: '21F-cul13ova_762763_premix.seq.clipped', reverse: '21R-cul13ova_762763_premix.seq.clipped' },
    { forward: '22F-Fi-14_semi_762763_premix.seq.clipped', reverse: '22R-Fi-14_semi_762763_premix.seq.clipped' },
    { forward: '23F-Fi-14p23_762763_premix.seq.clipped', reverse: '23R-Fi-14p23_762763_premix.seq.clipped' },
    { forward: '24F-CC37A_762763_premix.seq.clipped', reverse: '24R-CC37A_762763_premix.seq.clipped' },
    { forward: '25F-P57p16_762763_premix.seq.clipped', reverse: '25R-P57p16_762763_premix.seq.clipped' },
    { forward: '26F-P57p35_762763_premix.seq.clipped', reverse: '26R-P57p35_762763_premix.seq.clipped' },
    { forward: '27F-Fi-14_semi_Hsp83_premix.seq.clipped', reverse: '27R-Fi-14_semi_Hsp83_premix.seq.clipped' },
    { forward: '28F-Fi-14p23_Hsp83_premix.seq.clipped', reverse: '28R-Fi-14p23_Hsp83_premix.seq.clipped' },
    { forward: '29F-CC37A_Hsp83_premix.seq.clipped', reverse: '29R-CC37A_Hsp83_premix.seq.clipped' },
    { forward: '30F-CC49A_Hsp83_premix.seq.clipped', reverse: '30R-CC49A_Hsp83_premix.seq.clipped' },
    { forward: '31F-cul13_LSU_premix.seq.clipped', reverse: '31R-cul13_LSU_premix.seq.clipped' },
    { forward: '32F-cul13ova_LSU_premix.seq.clipped', reverse: '32R-cul13ova_LSU_premix.seq.clipped' },
    { forward: '33F-Fi-14_semi_LSU_premix.seq.clipped', reverse: '33R-Fi-14_semi_LSU_premix.seq.clipped' },
    { forward: '34F-Fi-14p23_LSU_premix.seq.clipped', reverse: '34R-Fi-14p23_LSU_premix.seq.clipped' },
    { forward: '35F-CC37A_LSU_premix.seq.clipped', reverse: '35R-CC37A_LSU_premix.seq.clipped' },
    { forward: '35F-CC37A_LSU_premix#2.seq.clipped', reverse: '35R-CC37A_LSU_premix#2.seq.clipped' },
    { forward: '36F-P57p16_LSU_premix.seq.clipped', reverse: '36R-P57p16_LSU_premix.seq.clipped' },
    { forward: '37F-P57p35_LSU_premix.seq.clipped', reverse: '37R-P57p35_LSU_premix.seq.clipped' },
    { forward: '38F-cul13ova_catalase_premix.seq.clipped', reverse: '38R-cul13ova_catalase_premix.seq.clipped' }
]

folder = '/home/anna/Dropbox/phd/bioinformatics/genomes/kinetoplastids/Blastocrithidia_P57/Eurofins/new/sequences_together/merging/'
Dir.chdir folder

merge_list.each do |seq_pair|
    name = seq_pair[:forward][0..-13]

    fasta_forward = folder + seq_pair[:forward]
    fasta_reverse = folder + seq_pair[:reverse]

    alignment = "#{name}.alignment"
    fasta = "#{name}_merged.fasta"

    `merger #{fasta_forward} #{fasta_reverse} #{alignment} #{fasta} -sreverse2`
end
