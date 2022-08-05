
list_los = [1, 2, 3, 4, 5, 6, 7]
los = 2.5
x = 1000
for i in range(len(list_los)):
    if abs(list_los[i] - los) < x:
        x = abs(list_los[i] - los)
        ind_los_i = i
print(ind_los_i)