def BMI(a1,a2):
    a3=round(a2/((a1*a1)*0.0001),2)
    print(a3)
    if a3<=24 and a3>=18.5 :
        print('正常範圍')
    elif a3<18.5:
        print('體重過輕')
    else:
        print('異常範圍')

a1=int(input('輸入身高(cm):'))
a2=int(input('輸入體重(kg):'))
BMI(a1,a2)