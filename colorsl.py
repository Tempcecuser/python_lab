clist1=set()
clist2=set()
n1=int(input("Enter the number of colors in the list1:"))
print("enter the colors to list1:")
for x in range(n1):
    color=input()
    clist1.add(color)
n2=int(input("Enter the number of colors in list2:"))
print("enter the colors to list2:")
for x in range(n2):
    color=input()
    clist2.add(color)
diff=clist1.difference(clist2)
print("colors in list 1 not in list 2",diff)
