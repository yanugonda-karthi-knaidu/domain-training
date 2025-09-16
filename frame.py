a=5
grid=[['A' for i in range(a+2)]for i in range(a+2)]

for i in range(a+2):
    for j in range(a+2):
        if (i==0 or j==0 or i==a+1 or j==a+1):
            grid[i][j]="A"
        elif(i%2!=0):
            grid[i][j]="*"
        else:
            grid[i][j]="$"
    
for i in range(a+2):
    for j in range(a+2):
        print(grid[i][j],end=' ')
    print()
