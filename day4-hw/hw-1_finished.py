#!/usr/bin/env python3
import sys
from fasta_iterator_class import FASTAReader
# get arguments from the command line

target_fname = sys.argv[1]
droyak_fname = sys.argv[2]
k = int(sys.argv[3])
# Load sequences

target_seqs = FASTAReader(open(target_fname))
droyak_seqs = FASTAReader(open(droyak_fname))



# for seq_id, sequence in droyak_seqs:
#     print(seq_id) # the NAME of the sequence in the FASTA file; a string
#     print(sequence) # FULL SEQUENCE of the sequence in the FASTA file; a string
# find 11bp sequences in Droyak fasta file
# that match to sequences in the subset.fa file

# turn target file into a dictionary
kmers = {}

for seq_id, sequence in target_seqs:
    for i in range(0, len(sequence) - k + 1):
        kmer = sequence[i:i + k]
       # kmers.setdefault(kmer, 0)
        if kmer in kmers:
            kmers[kmer].append(seq_id)
            kmers[kmer].append(i)
        else: 
            kmers[kmer] = [seq_id, i] 
count=0            
for seq_id, sequence in droyak_seqs:
    for i in range(0, len(sequence) - k + 1):
        kmer_query = sequence[i:i + k]
        if kmer_query in kmers:
            print("target sequence names and starts {}, query start: {}, kmer: {}".format(str(kmers[kmer_query]), i, kmer_query))
            count += 1
        if count >= 1000:
            break
            
            
# for key, value in kmers.items():
#     print(key, value)


#make kamers