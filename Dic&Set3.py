#Create an empty dictionary. Allow 4 friends to enter their favorite language as 
#value and use key as their names. Assume that the names are unique. 
friends = {}

for i in range(4):
    name = input("Enter your name: ")
    lang = input("Enter your favorite language: ")
    friends[name] = lang

print("\nFavorite languages:", friends)
#If the names of 2 friends are same; what will happen ?
friends = {'A': 'Python'}
friends['A'] = 'Java'
print(friends)
#Output: {'A': 'Java'}
#In the above code, since the key 'A' is used twice, 
# the second assignment will overwrite the first one. 
# Therefore, the final output will be {'A': 'Java'}, 
# and the original value 'Python' will be lost. 


#If languages of two friends are same; what will happen to the program ?
friends = {'A': 'Python', 'B': 'Python'}
print(friends)
#Output: {'A': 'Python', 'B': 'Python'}
#In this case, since the keys 'A' and 'B' are different,
# both friends can have the same favorite language 'Python' 
# without any issues.