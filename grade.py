'''Write a program to calculate the grade of a student
 from his marks from the following scheme: 
 90 – 100 => Ex 
 80 – 90 => A 
 70 – 80 => B 
 60 – 70  =>C 
 50 – 60 => D 
 <50        
=> F'''
# Input marks for 3 subjects
marks = []
for i in range(3):
    mark = float(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculate average marks
average = sum(marks) / len(marks)

# Determine grade
if average >= 90:
    grade = "Ex"
elif average >= 80:
    grade = "A"
elif average >= 70:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "F"

print(f"The grade of the student is: {grade}")
