stu=["karthik", "mahesh", "ravi","adil", "bhuvanesh"]
marks=[[50,60,70,80],[30,40,70,90],[60,29,26,13],[23,67,87,90],[24,78,98,45]]
per=[]
for i in marks:
   a=sum(i)//3
   per.append(a)
for i in range(5):
    print("{}. {} : {}".format(i+1,stu[i].upper(),per[i]))
