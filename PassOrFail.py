#Write a program to find out whether a student has passed or failed if it requires a 
#total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
#take marks as an input from the user.
# Input marks for 3 subjects
marks = []
for i in range(3):
    mark = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(mark)

# Calculate total and percentage
total = sum(marks)
percentage = (total / 300) * 100

# Check if student has passed or failed
if percentage >= 40:
    print("The student has passed.")
else:
    print("The student has failed.")