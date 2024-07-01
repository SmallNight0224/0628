y = int(input("请输入你的身高: "))
x = int(input("请输入你的體重: "))
z = round(x/(y*0.01)**2,2)
print(z)
if z < 18.5:
    print("過輕")
elif z < 24:
    print("正常")
else:
    print("過重")
 
### 退出提示
input("点击 enter 键退出")
