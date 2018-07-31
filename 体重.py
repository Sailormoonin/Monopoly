while True:
    height = float(input('请输入身高: '))
    weight = float(input('请输入体重: '))
    best = height - 105
    if weight > best:
        print('偏胖')
    if weight == best:
        print('完美')
    if weight < best:
        print('偏瘦')
