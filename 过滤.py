f=[]
for i in open('filter.txt'):
    f.append(i.rstrip())
text = input('������һ�仰: ')
for each in f:
    if each in text:
        text =text.replace(each,'**')
else:
    print(text)
