import random
a=['A1','A2','A3','A4']

close=0
while close !=1:    
    a1=random.choice(a)
    print('**1',a1,'***')

    if a1=='A1':        
        a2=random.choice(a)
        print('**2',a2,'***')
        if a2=='A1':
            print('=====get A1=====')
            close+=1
            break

    elif a1=='A2':        
        a3=random.choice(a)
        print('**3',a3,'***')
        if a3=='A2':
            print('=====get A2=====')
            close+=1
            break

    elif a1=='A3':        
        a4=random.choice(a)
        print('**4',a4,'***')
        if a4=='A3':
            print('=====get A3=====')
            close+=1
            break

    elif a1=='A4':        
        a5=random.choice(a)
        print('**5',a5,'***')
        if a5=='A4':
            print('=====get A4=====')
            close+=1
            break
        