# 作者: 张浩然
# 2022年06月14日19时53分42秒
list_ = [25, 36, 12, 35, 15, 85, 95, 65, 45]
print(sorted(list_))
print(list_)
print(sorted({1: 'D', 2: 'A', 5: 'B', 2: 'C', 3: 'F', 4: 'G'}))
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10)]
print(sorted(student_tuples, key=lambda s: s[2]))


class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        # repr 返回 repr(任意可迭代对象)
        return repr([self.name, self.age, self.grade])


stu = [Student('张三', 71, 85),
       Student("王五", 95, 75),
       Student("kexing", 45, 35)]
print(sorted(stu, key=lambda s: s.age))
print(Student('王五', 75, 58))
from operator import itemgetter, attrgetter

print(sorted(stu, key=attrgetter('age')))
print(sorted(student_tuples, key=itemgetter(2)))
print(sorted(stu, key=attrgetter('age', 'grade')))
print(sorted(student_tuples, key=itemgetter(1,2)))
medict = {'Li': ['M', 7],
          'zhang': ['E', 2],
          'Wang': ['P', 3],
          'Du': ['C', 2],
          'Ma': ['C', 9],
          'Zhe': ['H', 7]}
# for i in medict:
    # print(i)
# print(sorted(medict.items(),key=lambda t:t[1][1]))

