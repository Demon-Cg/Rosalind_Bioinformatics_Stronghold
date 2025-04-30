def counting_dna(seq):
	A_count = seq.count('A')
	T_count = seq.count('T')
	C_count = seq.count('C')
	G_count = seq.count('G')
	return A_count, C_count, G_count, T_count 
if __name__ == '__main__':
	try:
		dna_seq = input('请输入DNA序列：').upper()
		counts = counting_dna(dna_seq)
		print(*counts)
	except ValueError as e:
		print(f'错误：{e}')
