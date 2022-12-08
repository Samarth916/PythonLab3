lst = []
n=int(input("enter the no of elements :"))
for i in range(0,n):
    el = int(input( ))
    lst.append(el)
print(lst)
lst.pop(0)
lst.pop(n-2)
print(lst)
