def prime_factor(n, i):
        if n<=1:
            return
        while (n%i!=0):
            i+=1
        print(i, end=" ")
        prime_factor(n//i, i)
            
        
n= int(input("enter the number: ")) 
i=2
prime_factor(n,i)
