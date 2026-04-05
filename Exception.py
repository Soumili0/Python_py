'''
Write a program to open three files 1.txt,
 2.txt and 3.txt if any these files are not 
present, a message without exiting 
the program must be printed prompting the same. 
'''
try:
    file1 = open('1.txt', 'r')
except FileNotFoundError:
    print("File 1.txt not found.")
try:    file2 = open('2.txt', 'r')
except FileNotFoundError:
    print("File 2.txt not found.")
try:    file3 = open('3.txt', 'r')
except FileNotFoundError:
    print("File 3.txt not found.")

                