#正序乘法表
for i in range(1,10):
    for j in range(1,i+1):
        print(str(i)+str("*")+str(j)+str("=")+str(i*j),end="   ")#end=" "代表不换行输出
    print() #换行

for i in range(1,10):
    for j in range(1,10):
        if(j<=i):
            print(str(j)+"*"+str(i)+"="+str(i*j),end="\t")
        else:
            break #跳出条件
    print() #换行

'''for a in range(9,0,-1):
    print(a)'''

#逆序乘法表
for i in range(9,0,-1):
    for j in range(1,i+1):
        print(str(i)+str("*")+str(j)+str("=")+str(i*j),end="\t")#end=" "代表不换行输出
    print() #换行

for i in range(9,0,-1):
    for j in range(1,10):
        if(j>0 and j<=i):
            print(str(j)+"*"+str(i)+"="+str(i*j),end="\t")
        else:
            break #跳出条件
    print() #换行