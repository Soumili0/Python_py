'''A spam comment is defined as a text containing following keywords: 
“Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program 
to detect these spams.'''
# Define spam keywords
spam_keywords = ["Make a lot of money", "buy now", "subscribe this", "click this"]
# Take input from user
comment = input("Enter a comment: ")
# Check for spam
is_spam = any(keyword in comment for keyword in spam_keywords)
if is_spam:
    print("This comment is detected as spam.")
else:    print("This comment is not spam.")
