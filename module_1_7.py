grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = (sum(grades[0]) / len(grades[0]))
b = (sum(grades[1]) / len(grades[1]))
c = (sum(grades[2]) / len(grades[2]))
d = (sum(grades[3]) / len(grades[3]))
e = (sum(grades[4]) / len(grades[4]))

students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students_sort = sorted(list(students))
_dict = {}
_dict[students_sort[0]] = (sum(grades[0]) / len(grades[0]))
_dict[students_sort[1]] = (sum(grades[1]) / len(grades[1]))
_dict[students_sort[2]] = (sum(grades[2]) / len(grades[2]))
_dict[students_sort[3]] = (sum(grades[3]) / len(grades[3]))
_dict[students_sort[4]] = (sum(grades[4]) / len(grades[4]))

print(_dict)
# average_score = {['a' + 'b']}
# print(average_score)