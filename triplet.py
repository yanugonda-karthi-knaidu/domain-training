def cop(a,b):
     return gcd(a,b)==1 
 
def gcd(a,b):
    while(b!=0):
        rem=a%b
        a=b
        b=rem
    return a
       
n=int(input("enter the number: "))
for i in range(5,n):
    for j in range (4,i):
        for k in range(3,j):
            if j*j + k*k ==i*i and cop(i,j) and cop(j,k) and cop(k,i): 
                print(f"triplet is {k},{j},{i}")
            

    
    
