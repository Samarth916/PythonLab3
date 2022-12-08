# Write your code here :-)
lst=[]
n=int(input("enter the no of elements"))
for i in range(0,n):
    el = int(input())
    lst.append(el)
print(lst)
sum=[]
sum.append(lst[0])
for i in range(1,n):
    s=lst[i-1]+lst[i]
    sum.append(s)
print(sum)
