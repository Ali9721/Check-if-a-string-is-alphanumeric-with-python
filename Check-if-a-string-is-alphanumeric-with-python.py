# Define "text" as a variable & gets string.
text = input("Please enter a string: ")

# Use "if" & "else" & "isalnum" 
if text.isalnum():
# Output the result in this condition.
    print(f"{text} is alphanumeric.")
else:
# Output the result in this condition. 
    print(f"{text} is not alphanumeric.")