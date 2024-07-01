import random
def x(a1,a2):
    print('-加法練習-')
    a3=a1+a2
    print(a1,'+',a2,'=?')
    b=int(input('輸入答案:'))
    if a3==b:
        print('答對')
    else:
        print('答錯')

a1=random.randint(1,10)
a2=random.randint(1,10)
x(a1,a2)