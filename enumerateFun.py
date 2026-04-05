'''
 Write a program to print third, fifth and 
 seventh element from a list using enumerate 
 function. 
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for index, value in enumerate(my_list):
    if index == 2:  # Third element (index starts from 0)
        print(f"Third element: {value}")
    elif index == 4:  # Fifth element
        print(f"Fifth element: {value}")
    elif index == 6:  # Seventh element
        print(f"Seventh element: {value}")
        