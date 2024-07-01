import random
print('-加法練習-')
a1=random.randint(1,10)
a2=random.randint(1,10)
a3=a1+a2
print(a1,'+',a2,'=?')

b=int(input('輸入答案:'))

close=0
while close !=2:
    if a3==b:
        close=1
        print('答對')
        break    

    else:
        close+0=0
        b=int(input('輸入答案:'))
        print('答錯')
        