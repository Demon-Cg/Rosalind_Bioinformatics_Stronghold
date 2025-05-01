def find_dna_motif(seq, motif):
    positions = []
    pos = seq.find(motif)
    while pos != -1:
        positions.append(pos + 1)
        pos = seq.find(motif , pos + 1 )
    if positions != []:
        return(positions)
    else:
        return('无')

if __name__ == '__main__':
    try:
        dna_seq = input('请输入DNA序列：').upper().strip()
        dna_motif = input('请输入想寻找的motif：').upper().strip()
        motif_position = find_dna_motif(dna_seq, dna_motif)
        print(*motif_position)
    except ValueError as e:
        print(f'错误：{e}')