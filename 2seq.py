lst2 = []
s = input("Введите элементы списка через запятую: ")
lst = s.split(',')
for i in lst:
    if lst.count(i) == 1:
        lst2.append(int(i))
print(lst2)