import random
output = []
while(len(output)!=5):
    d=random.randint(1, 10)
    if(d not in output):
        output.append(d)
print(output)
