def nested_list(t):
    total = 0
    for i in t:
       total = total + sum(i)
    return total

t = [[1,2],[3],[4,5,6]]
res = nested_list(t)
print(res)
