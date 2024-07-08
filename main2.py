# исходные данные
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# преобразование множества в отсортированный список
students = list(students)
sorted_students = sorted(students)

# вычисление среднего значения
average_grades = [sum(grade) / len(grade) for grade in grades]

# создание словаря
dict_= dict(zip(sorted_students, average_grades))
print(dict_)
