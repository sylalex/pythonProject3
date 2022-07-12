lst1 = []
lst2 = []
s = input("Введите элементы 1-го списка через запятую: ")
lst = s.split(',')
for i in lst:
    lst1.append(int(i))
s = input("Введите элементы 2-го списка через запятую: ")
lst = s.split(',')
for i in lst:
    lst2.append(int(i))
for i in lst2:
    lst1.remove(i)
print(lst1)
