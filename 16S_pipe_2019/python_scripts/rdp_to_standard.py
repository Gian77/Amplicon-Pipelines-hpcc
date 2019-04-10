####
#	Written by Natalie Vande Pol, Feb 26, 2019
#
#	Script converts RDP output taxonomy to standard output for BACTERIA
####

# make a table with the following columns
# OTU# domain, phylum, class, subclass, order, suborder, family, genus (ID & confidence for each)


import sys, os, itertools

input = open ("otus_taxonomy_RDP.rdp", "r")
all_lines = input.readlines()
input.close()

output = open("otus_taxonomy_RDP_std-fmt.rdp", "w")
output.write("OTU_ID\tDomain\tD_Score\tPhylum\tP_Score\tClass\tC_Score\tSubclass"
             "\tSC_Score\tOrder\tO_Score\tSuborder\tSO_Score\tFamily\tF_Score\tGenus\tG_Score\n")
all_levels=["domain","phylum","class","subclass","order","suborder","family","genus"]
for i, line in enumerate(all_lines):
	# capture confidence level at genus before changing line
	temp = line.strip().replace("\"","").split("\t")
	confi = temp[7:-2][::3]
	confi.append(temp[-1])
	taxon = temp[5:][::3]
	level = temp[6:][::3]

	if len(taxon)!=len(level):
		print temp[0]
		print taxon
		print level
	if len(confi) != len(taxon):
		print temp[0]
		print taxon
		print confi

	output.write(temp[0]+"\t")
	k=0
	for j in all_levels:
		if j == level[k]:
			output.write(taxon[k]+"\t"+confi[k]+"\t")
			k+=1
		else:
			output.write("NA"+"\t"+"NA"+"\t")
	output.write("\n")

output.close()
