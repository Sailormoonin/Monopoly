while True:
    ins = float(input('please input your instance��'))
    if ins <= 0:
        print('��������������������룺')
        break
    else:
        if ins <= 2 and ins > 0:
            cost = 16
            print(cost)
        if ins >2 and ins <= 12:
            cost = 8 + (ins - 2) * 1.2
            print(cost)
        if ins > 12:
            cost = 8 +(12 - 2) * 1.2 + (ins -12)*1.5
            print(cost)
    
