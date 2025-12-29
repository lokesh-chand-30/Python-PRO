student = {'name':'lokesh', 'roll_no':'30','faculty':'BCT','semester':'5th','marks[5]':'90 92 94 95 95'}
print(student)
student = {}
student['name'] = input("Enter name: ")
student['roll_no'] = input("Enter roll number: ")
student['faculty'] = input("Enter faculty: ")
student['semester'] = input("Enter semester: ")
marks_list = []
for i in range(1,6):
    marks= input(f"Enter marks for subject{i}:")
    marks_list.append(int(marks))
print(marks_list)
student['marks']=marks_list
total_obtained=sum(marks_list)
percentage= (total_obtained *100)/500
print(f"Percentage:{percentage:.2f}%")
student['percentage']=percentage
if percentage>=40:
    student["result"]="Pass"
else:
    student["result"]="Fail"
print(student)