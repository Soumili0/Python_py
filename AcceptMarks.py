marks = []
for i in range(6):
    m = int(input(f"Enter the marks of subject {i+1}: "))
    marks.append(m)
    marks.sort()
print("The marks you entered in sorted order are:", marks)
#Enter the marks of subject 1: 78
#Enter the marks of subject 2: 96
#Enter the marks of subject 3: 90
#Enter the marks of subject 4: 56
#Enter the marks of subject 5: 91
#Enter the marks of subject 6: 83
#The marks you entered in sorted order are: [56, 78, 83, 90, 91, 96]
