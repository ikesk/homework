# 42dust.py

# Write a program that performs entropy filtering on nucleotide fasta files
# Windows that are below the entropy threshold are replaced by N

# Program arguments include file, window size, and entropy threshold

# Output should be a fasta file with sequence wrapped at 60 characters

# Hint: use the mcb185 library
# Hint: make up some fake sequences for testing

# Note: don't worry about "centering" the entropy on the window (yet)
import math
import sys
import mcb185


def calculate_entropy(seq):
    # Count occurences of each base
    base_counts = {}
    for base in seq:
        if base in base_counts:
            base_counts[base] += 1
        else:
            base_counts[base] = 1

    # Calculate probabilities for each base
    probabilities = {}
    for base in base_counts:
        probabilities[base] = base_counts[base] / len(seq)

    # Calculate entropy using Shannon's entropy
    entropy = 0
    for base in probabilities:
        p = probabilities[base]
        entropy += -(p * math.log2(p))
    return entropy


def wrap_sequence(seq):
    # If sequence is short, no change required
    if len(seq) <= 60:
        return seq
    else:
        # Initialize list to store wrapped lines
        wrapped_lines = []

        # Iterate over sequence in steps of 60 chars
        for i in range(0, len(seq), 60):
            line = seq[i : i + 60]
            wrapped_lines.append(line)

        # Join lines into a string separated by newlines
        wrapped_seq = "\n".join(wrapped_lines)
    return wrapped_seq


# Process user input
file = sys.argv[1]
w = int(sys.argv[2])
threshold = float(sys.argv[3])

# Modify the sequence based on user input
for defline, seq in mcb185.read_fasta(file):

    # Convert sequence into list for modifications
    modified_seq = list(seq)

    # Apply entropy filtering 
    for i in range(0, len(seq) - w + 1):
        window = seq[i : i + w]
        entropy = calculate_entropy(window)
        if entropy < threshold:
            modified_seq[i : i + w] = 'N' * w
    new_seq = wrap_sequence("".join(modified_seq))

# Write modified sequence to the output file in fasta format
with open("42dust_output.fna", 'w') as fp:
    fp.write(f'>{defline}\n{new_seq}\n')


"""
python3 42dust.py ~/DATA/E.coli/GCF_000005845.2_ASM584v2_genomic.fna.gz 11 1.4
>NC_000913.3 Escherichia coli str. K-12 substr. MG1655, complete genome
AGNNNNNNNNNNNGACTGCAACGGGCAATATGTCTCTGTGTNNNNNNNNNNNNNNNNNTC
TGATAGCAGCTTCTGAACTGGTTACCTGCCGTGNNNNNNNNNNNNNNNNNNNNNCTTAGG
TCACNNNNNNNNNNNNCCAATATAGGCATAGCGCACAGNNNNNNNNNNNNNNNNGAGTNN
NNNNNNNNNNTGAAACGCATTAGCACCACCATNNNNNNNNNNNNNNNNNTTACCACAGGT
AACNNNNNNNNNNNACGCGTACAGNNNNNNNNNNNNNNNNNNCGCACCTGACAGTGCNNN
NNNNNNNNNNNNNCCAAAGGTAACGAGGTAACAACCATGCGAGTGTTGAAGTTCGGCGGT
ACATCAGTGGCAAATGCAGAACGTTTTCTGCGTGTTGCCGATATTCTGGAAAGCAATGCC
ANNNNNNNNNNNNNNNCCANNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNNGGTG
GCGATNNNNNNNNNNNNNNNNNGCGGCCAGGATGCTTTACCCAATATCAGCGATGCCGAA
...
"""
