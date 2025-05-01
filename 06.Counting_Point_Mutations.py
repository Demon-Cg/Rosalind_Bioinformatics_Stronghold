def hamming_distance(seq1, seq2):
	hamming_distance = sum(seq1 != seq2 for seq1 , seq2 in zip (seq1 , seq2))
	return hamming_distance
if __name__ == '__main__':
	try:
		dna_seq1 = input('请输入第一条序列：')
		dna_seq2 = input('请输入第二条序列：')
		distance = hamming_distance(dna_seq1, dna_seq2)
		print(distance)
	except ValueError as e:
		print(f'错误：{e}')