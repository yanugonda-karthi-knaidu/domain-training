a=str(input("enter a string: "))
res=""
c=1
for i in range (len(a)):
    if (i+1<len(a) and a[i]==a[i+1]):
        c+=1
    else:
        res=res+a[i]
        res +=str(c)
        c=1
print(res)
