print('成績分級')
x=int(input('分數:'))
if x>=101:
    print('錯誤')
elif x>=80:
    print('A')
elif x>=70:
    print('B')
elif x>=60:
    print('C')
else:
    print('D')
