n1=int(input("Enter no. Of elements:"))
list_number=[]
n=int(input("enter the no of rotations:"))
#read list of values from user
for i in range(n1):
    num=int(input())
    #append number to list data structure
    list_number.append(num)
print(list_number)
list_number = (list_number[-n:] + list_number[:-n])
print(list_number)

#output
Enter no. Of elements:5
enter the no of rotations:2
13
16
25
9
125
[13, 16, 25, 9, 125]
[9, 125, 13, 16, 25]
