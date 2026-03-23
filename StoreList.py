#program to store seven fruits in a list entered by user
fruits= []
for i in range(7):
    fruit = input(f"Enter the name of fruit {i+1}: ")
    fruits.append(fruit)
print("The list of fruits you entered is:", fruits)
#Enter the name of fruit 1: apple
#Enter the name of fruit 2: mango
#Enter the name of fruit 3: banana
#Enter the name of fruit 4: orange
#Enter the name of fruit 5: grapes
#Enter the name of fruit 6: cucumber
#Enter the name of fruit 7: papaya
#The list of fruits you entered is: ['apple', 'mango', 'banana', 'orange', 'grapes', 'cucumber', 'papaya']