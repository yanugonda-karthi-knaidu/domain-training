import random
no=int(input("enter no of teams: "))
teams=[]
matches=[]
for i in range(no):
    d=input("enter the team name: ")
    teams.append(d)
vs=int(input("enter no of matches btw same team: "))
for i in range(no-1):
    for j in range(i+1,no):
        for k in range(vs):
            matches.append([teams[i],teams[j]])
random.shuffle(matches)
for i in range(len(matches)):
    print("match {}. {} vs {}".format(i+1,matches[i][0],matches[i][1]))
