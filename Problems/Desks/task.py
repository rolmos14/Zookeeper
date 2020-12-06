# put your python code here
students_class_1 = int(input())
students_class_2 = int(input())
students_class_3 = int(input())

min_desks_required = students_class_1 // 2 + students_class_1 % 2 \
                    + students_class_2 // 2 + students_class_2 % 2 \
                    + students_class_3 // 2 + students_class_3 % 2

print(min_desks_required)