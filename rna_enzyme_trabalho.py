from Bio import SeqIO

def main():
    a = SeqIO.parse("rna_structures/opuntia.fa", "fasta")
    
    for seq_record in a:
        print(seq_record)
        print(seq_record.id)
        print(repr(seq_record.seq))
        print(len(seq_record))

def parse_enzyme():
    pass

def generate_secondary_rna():
    pass

if __name__ == '__main__':
    print("testing sequence")
    main()