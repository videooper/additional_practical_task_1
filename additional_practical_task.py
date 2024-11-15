# На вход даны следующие данные:

# Списки с оценками
grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]

# Множество студентов
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

# Сортировка студентов
list_students = sorted(students)

# Вычисляем средние баллы
average = [sum(grade) / len(grade) for grade in grades]

# Создаем словарь со средними баллами
students_average = {list_students[i]: average[i] for i in range(len(list_students))}

#Вывод в консоль
print(students_average)