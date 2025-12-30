marks = [78, 85, 92, 66, 88, 95, 71, 83]
print("The average of marks is:",sum(marks)/len(marks))
print("The max marks among the list is:",max(marks))
print("The min marks among the list is:",min(marks))
count=0
for i in marks:
    if i >= 80:
        count+=1
print("Distinction count:",count)

grades = []
for m in marks:
    if m >= 90:
        grades.append("A+")
    elif m >= 80:
        grades.append("A")
    elif m >= 70:
        grades.append("B")
    else:
        grades.append("C")
print("Student grades:", " ".join(grades))


    
