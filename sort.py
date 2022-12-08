lst = []
n=int(input("enter the no of elements :"))
for i in range(0,n):
    el = int(input())
    lst.append(el)
print(lst)
def sort(lst):
    new=sorted(lst)
    if (new==lst):
        print("True")
    else:
        print("False")
sort(lst)
