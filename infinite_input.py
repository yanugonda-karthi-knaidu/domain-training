a=1
sum=0
while(a!=0):
    a=int(input("enter amount in Rs: "))
    if(a>=40 and a<=100):
        continue
    sum=sum+a
print(sum)
