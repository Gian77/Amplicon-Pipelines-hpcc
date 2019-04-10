#!/usr/bin/env python

import sys

reads = sys.argv[1]
index = sys.argv[2]

all_readIDs = set()

# Re-written the code below to only ever read the first row:
with open(reads, "r") as read_file:
	while True:
		try:
			line1 = next(read_file)
			temp = line1.split()
			if line1.startswith("@M03127"): all_readIDs.add(temp[0])
			next(read_file) # We walk through the
			next(read_file) # next 3 lines but don't
			next(read_file) # save the data anywhere. 
		except StopIteration:
			break
# This hasn't changed:
if not all_readIDs: print "List is Empty"
else:
	for idx,item in enumerate(all_readIDs):
		print item
		if idx == 10: break

# Rewritten to not skip any rows and write all 4 rows to a file if the ID line in the ID set:
with open(index, "r") as index_file, open("filtered_index.fastq", "w") as filtered_file:
	while True:
		try:
			line1 = next(index_file).strip()
			line2 = next(index_file)
			line3 = next(index_file)
			line4 = next(index_file)
		except StopIteration:
			break
		if line1[:-8] in all_readIDs:
			filtered_file.write(line1+"\n")
			filtered_file.write(line2)
			filtered_file.write(line3)
			filtered_file.write(line4)
print "All done!"

