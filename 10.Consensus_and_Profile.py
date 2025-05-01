from collections import Counter

def read_fasta(fasta_file):
    seqs = {}
    with open(fasta_file, 'r') as file:
        current_id = ''
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                current_id = line[1:]
                seqs[current_id] = ''
            else:
                seqs[current_id] += line
    return list(seqs.values()) 

def count_positions(sequences):
    position_counts = []
    seq_length = len(sequences[0]) 
    for _ in range(seq_length):
        position_counts.append(Counter())
    
    for seq in sequences:
        for pos, base in enumerate(seq):
            position_counts[pos][base] += 1
    return position_counts

def get_consensus(position_counts):
    return ''.join([counter.most_common(1)[0][0] for counter in position_counts])

def main(fasta_file):
    sequences = read_fasta(fasta_file)
    position_counts = count_positions(sequences)
    consensus = get_consensus(position_counts)
    print(f"{consensus}")
    
    bases = ['A', 'C', 'G', 'T']
    for base in bases:
        counts = [str(position_counts[pos].get(base, 0)) for pos in range(len(position_counts))]
        print(f"{base}: {' '.join(counts)}") 
if __name__ == '__main__':
    fasta_file = input('请输入fasta文件路径：').strip()
    try:
        main(fasta_file)
    except Exception as e: 
        print(f'错误：{e}')