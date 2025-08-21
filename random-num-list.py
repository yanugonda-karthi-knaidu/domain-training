l=[]
while (len(l)<5):
    a=int(input("Enter a number: "))
    if (a not in l):
        l.append(a)
    elif (a in l):
        print("Number already taken, please enter a different number.")
    
print(l)
        
