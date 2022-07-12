el_count = int(input("Введите количество элементов: "))
lst = []
for i in range(el_count):
    j = int(input(f"Введите {i+1} элемент: "))
    lst.append(j)
lst.sort()
print(lst)