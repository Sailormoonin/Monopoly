print('男生信息:\n')
m_age = int(input('请输入年龄: '))
m_height = float(input('请输入身高: '))
m_weight = float(input('请输入体重: '))
m_income = int(input('请输入收入: '))
print('女生信息:\n')
f_age = int(input('请输入年龄: '))
f_height = float(input('请输入身高: '))
f_weight = float(input('请输入体重: '))
f_income = int(input('请输入收入: '))
if 20>= f_age >28 and 160>= f_height >=175 and 40>= f_weight >=60 and 2000>= f_income >=5000:
    if 20>= m_age >28 and 170>= m_height >=185 and 55>= m_weihgt >75 and 2000>= m_income >5000:
        print('配对成功！')
else:
    print('配对失败！')

