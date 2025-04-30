def rabbit_relation(n, k):
    a, b = 1, 1
    for i in range(2, n):
        total = a + b * k
        b = a
        a = total
    return total

if __name__ == '__main__':
    try:
        # 正确输入方式：先获取输入，再分割和转换类型
        n, k = map(int, input('请输入n，k并用空格分隔：').split())
        result = rabbit_relation(n, k)
        print(result)
    except ValueError as e:
        print(f'错误：{e}')