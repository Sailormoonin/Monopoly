while True:
    height = float(input('���������: '))
    weight = float(input('����������: '))
    best = height - 105
    if weight > best:
        print('ƫ��')
    if weight == best:
        print('����')
    if weight < best:
        print('ƫ��')
