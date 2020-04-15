from Bio import SeqIO


def preprocess():
    data_raw = SeqIO.parse('./data/uniprot_sprot.fasta', 'fasta')
    for i, data in enumerate(data_raw):
        file_to_write = './data/uniprot_sprot_{}.txt'.format(i // 50000 + 1)
        with open(file_to_write, 'a') as f:
            f.write(str(data.seq) + '\n')


if __name__ == '__main__':
    preprocess()
