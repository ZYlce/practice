#待改正
i=0
while i<10:
    name = input("请输入学生的姓名：")
    grade = int(input("请输入学生的成绩："))
    student = []
    studentgood = []
    studentbad = []
    if grade>60:
        student.append(name)
        student.append(grade)
        studentgood.append(student)
    else:
        student.append(name)
        student.append(grade)
        studentbad.append(student)
    i = i+1
    print(i)
    student.clear()
print(student)
print(studentgood)
print(studentbad)
exit()
