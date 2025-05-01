import re

class Protein:
    def __init__(self):
        self.__pro_dic = {
            'GCU':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A', 'CGU':'R', 'CGC':'R',
            'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R', 'UCU':'S', 'UCC':'S',
            'UCA':'S', 'UCG':'S', 'AGU':'S', 'AGC':'S', 'AUU':'I', 'AUC':'I',
            'AUA':'I', 'UUA':'L', 'UUG':'L', 'CUU':'L', 'CUC':'L', 'CUA':'L',
            'CUG':'L', 'GGU':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G', 'GUU':'V',
            'GUC':'V', 'GUA':'V', 'GUG':'V', 'ACU':'T', 'ACC':'T', 'ACA':'T',
            'ACG':'T', 'CCU':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P', 'AAU':'N',
            'AAC':'N', 'GAU':'D', 'GAC':'D', 'UGU':'C', 'UGC':'C', 'CAA':'Q',
            'CAG':'Q', 'GAA':'E', 'GAG':'E', 'CAU':'H', 'CAC':'H', 'AAA':'K',
            'AAG':'K', 'UUU':'F', 'UUC':'F', 'UAU':'Y', 'UAC':'Y', 'AUG':'M',
            'UGG':'W', 'UAG':'', 'UGA':'', 'UAA':''
        }

    def is_valid_rna(self, seq):
        #检查RNA序列（仅含AUCG）
        return bool(re.fullmatch(r'^[AUCG]+$', seq.upper()))

    def rna_to_protein(self, rna):
        #检查RNA序列
        if not self.is_valid_rna(rna):
            raise ValueError("Invalid RNA sequence: must contain only A, U, C, G.")

        #检查序列长度是否为3的倍数
        if len(rna) % 3 != 0:
            raise ValueError("RNA length must be a multiple of 3.")

        #分割密码子并翻译
        codons = re.findall(r'.{3}', rna.upper())
        protein = []
        for codon in codons:
            if codon not in self.__pro_dic:
                raise ValueError(f"Invalid codon: {codon}")
            protein.append(self.__pro_dic[codon])
        
        return ''.join(protein)

if __name__ == '__main__':
    p = Protein()
    try:
        rna_seq = input("请输入RNA序列: ").strip().upper()
        result = p.rna_to_protein(rna_seq)
        print(f"蛋白质序列: {result}")
    except ValueError as e:
        print(f"错误: {e}")