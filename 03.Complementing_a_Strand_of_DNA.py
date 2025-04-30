def dna_complementing(seq):
	reversed_seq = seq.lower()[::-1]
	complement = (
		reversed_seq
		.replace('a', 'T')
		.replace('c', 'G')
		.replace('g', 'C')
		.replace('t', 'A')
		)
	return complement
if __name__ == '__main__':
	try:
		dna_seq = input('请输入DNA序列：')
		complemented_seq = dna_complementing(dna_seq)
		print(complemented_seq)
	except ValueError as e:
		print(f'错误：{e}')
