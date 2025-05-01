def mendel_first_law(AA, Aa, aa):
    total = AA + Aa + aa
    num = 1 - (aa/total*(aa-1)/(total - 1) + 
               Aa/total * (Aa - 1)/(total -1)*0.25 + 
               Aa/total * aa/(total -1)*0.5 + 
               aa/total * Aa/(total - 1)*0.5)
    return round(num, 5)

# 获取输入并转换为整数
AA, Aa, aa = map(int, input('请输入AA，Aa，aa的值，并用空格分隔:').split())

# 调用函数并传递参数
result = mendel_first_law(AA, Aa, aa)
print(result)