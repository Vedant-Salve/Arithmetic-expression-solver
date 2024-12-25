#Arithmatic Calculator
#Made by Vedant
#Try not to get zero Division error
#Do not use two operators in continuity (ex. 2*+3, 2/-3)
print("Ex.: input: 50*2-8/4/2-19/19*5")
print("Output: 94")
a=input("Enter you Eqn: ").split('+')
print(a)
for i in range(len(a)):
    if "-" not in a[i]:
        if "*" in a[i]:
            if "/" not in a[i]:
                a[i]=a[i].split('*')
                print(a)
                m1=1
                for j in a[i]:
                    m1=m1*float(j)
                a[i]=m1
                print(a)
        if "/" in str(a[i]):
            if "*" not in str(a[i]):
                a[i]=a[i].split('/')
                print(a)
                d1=float(a[i][0])
                for dk in range(1,len(a[i])):
                    d1=d1/float(a[i][dk])
                a[i]=d1
                print(a)
        if "/" in str(a[i]):
            if "*" in str(a[i]):
                a[i]=a[i].split('*')
                print(a)
                for l5 in range(len(a[i])):
                    a[i][l5]=a[i][l5].split('/')
                    d4=float(a[i][l5][0])
                    for dk2 in range(1,len(a[i][l5])):
                        d4=d4/float(a[i][l5][dk2])
                    a[i][l5]=d4
                m4=1
                for l4 in range(len(a[i])):
                    m4=m4*float(a[i][l4])
                a[i]=m4
                print(a)
    elif "-" in str(a[i]):
        a[i]=a[i].split('-')
        print(a)
        for l in range(len(a[i])):
            if "*" in str(a[i][l]):
                if "/" not in str(a[i][l]):
                    a[i][l]=a[i][l].split('*')
                    m2=1
                    for k in a[i][l]:
                        m2=m2*float(k)
                    a[i][l]=m2
                    print(a)
            if "/" in str(a[i][l]):
                if "*" not in str(a[i][l]):
                    a[i][l]=a[i][l].split('/')
                    d2=float(a[i][l][0])
                    for dk2 in range(1,len(a[i][l])):
                        d2=d2/float(a[i][l][dk2])
                    a[i][l]=d2
                    print(a)
            if "/" in str(a[i][l]):
                if "*" in str(a[i][l]):
                    a[i][l]=a[i][l].split('*')
                    for l6 in range(len(a[i][l])):
                        print(a)
                        a[i][l][l6]=a[i][l][l6].split('/')
                        d7=float(a[i][l][l6][0])
                        for dk3 in range(1,len(a[i][l][l6])):
                            d7=d7/float(a[i][l][l6][dk3])
                        a[i][l][l6]=d7
                    m6=1
                    for l7 in range(len(a[i][l])):
                        m6=m6*float(a[i][l][l7])
                    a[i][l]=m6
                    print(a)
        print(a)
        if (type(a[i][0])==str):
            a[i][0]=0
        s7=a[i][0]
        for l4 in range(1,len(a[i])):
            s7=s7-float(a[i][l4])
        a[i]=s7
print(a)
s8=0
for lk in range(len(a)):
    s8=s8+float(a[lk])
a=s8
print(a)