import random
print('輸入1加法練習 輸入2乘法練習')
x=int(input('輸入號碼:'))

a1=random.randint(1,10)
a2=random.randint(1,10)
a3=a1+a2
a4=a1*a2

match x:
    case 1:
        print(a1,"+",a2,"=")
        b1=int(input('輸入答案:'))
        if a3==b1:
            print("答對")
        else:
            print("答錯")
    case 2:
        print(a1,"*",a2,"=")
        b2=int(input('輸入答案:'))
        if a4==b2:
            print("答對")
        else:
            print("答錯")
