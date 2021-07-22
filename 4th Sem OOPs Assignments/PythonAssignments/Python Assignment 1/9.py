#Use map and zip to find the elements-wise maximum amongest sequences of student list,subject list and marks list
# zip()
from functools import *
n=int(input("Enter number of instances:"))
name_list=[]
subject_list=[]
marks_list=[]
for i in range(n):
    name=input("Name: ")
    subject=input("Subject: ")
    marks=input("Marks: ")
    name_list.append(name)
    subject_list.append(subject)
    marks_list.append(marks)
combo_list=list(zip(name_list,subject_list,marks_list)) 
combo_list=reduce(lambda a,b: a if (a[2]>b[2]) else b, combo_list)   
print("Maximum elements: ")
print(combo_list)
