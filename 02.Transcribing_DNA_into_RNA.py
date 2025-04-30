def dna_to_rna(seq):
	T_to_U = seq.replace('T', 'U')
	return T_to_U
if __name__ == '__main__':
	try:
		dna_seq = input('请输入DNA序列：').upper()
		rna_seq = dna_to_rna(dna_seq)
		print(rna_seq)
	except ValueError as e:
		print(f'错误：{e}')
