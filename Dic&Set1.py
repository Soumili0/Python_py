# Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

# Create dictionary
hindi_dict = {
    "paani": "water",
    "aag": "fire",
    "hawa": "air",
    "mitti": "soil",
    "dost": "friend",
    "kitab": "book",
    "ghar": "house",
    "khana": "food"
}

# Show available words
print("Available Hindi words:")
for word in hindi_dict:
    print(word)

# Take input from user
user_input = input("\nEnter a Hindi word to find its English meaning: ")

# Lookup
if user_input in hindi_dict:
    print("Meaning:", hindi_dict[user_input])
else:
    print("Word not found in dictionary!")