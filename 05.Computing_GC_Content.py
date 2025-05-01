def read_fasta(fasta):
	seqs = {}
	with open(fasta_file, 'r') as file:
		current_id = None
		for line in file:
			line = line.strip()
			if line.startswith('>'):
				current_id = line[1:]
				seqs[current_id] = ''
			else:
				seqs[current_id] += line
	return seqs

def gc_content(seq):
	gc = seq.count('G') + seq.count('C')
	return (gc/len(seq)) * 100

def find_max_gc(fasta_file):
	seqs = read_fasta(fasta_file)
	max_gc = -1
	max_id = None
	max_seq = None

	for seq_id , seq in seqs.items():
		gc = gc_content(seq)
		if gc > max_gc:
			max_gc = gc
			max_id = seq_id
			max_seq = seq

	return max_id, max_gc

if __name__ == '__main__':
	fasta_file = input('请输入fasta文件路径：')
	try:
		max_id, max_gc = find_max_gc(fasta_file)
		print(max_id)
		print(f'{max_gc:.6f}')
	except ValueError as e:
		print(f'错误：{e}')
