from Bio import AlignIO

import argparse

def get_args():
    
    description = '''
    
    Return the consesus sequence of a given DNA protein or MSA.
    
    '''
    
    parser = argparse.ArgumentParser(description="Return the consesus sequence of a given DNA protein     or MSA.")

    parser.add_argument(
        "fasta_files",
        nargs=1,
        help="DNA protein or MSA in fasta format.",
        type=str,
        metavar="<fasta file>"
        )

    return parser.parse_args()


def get_consensus_seq(fasta_filename):
    
    result_name = fasta_filename.replace(
        ".fasta",
        "_consensus_seq.fasta"
        )
    
    with open(fasta_filename, "r") as myFile:
        result_file = open(result_name, "w")
        
        filename = (fasta_filename)
        format = "fasta"
        result = AlignIO.read(filename, format)
        result_file.write(str(result))
                
        result_file.close()
        
print("Processing files..")

args = get_args()
for file in args.fasta_files:
    get_consensus_seq(file)
    
print("DONE.")
