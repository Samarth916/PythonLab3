lst = []
n=int(input("enter the no of elements :"))
for i in range(0,n):
    el = int(input())
    lst.append(el)
print(lst)
def has_duplicate(lst):
    for i in range(0,n-1):
        s=lst.count(lst[i])
        if(s>1):
            print("True")
            break
has_duplicate(lst)
