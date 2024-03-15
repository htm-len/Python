#User input asking for name 
#Methods remove whitespace from str and capitlize user's name
name = input("\nWhat's your name ? ").strip().title()

#Split user's name into first name and last name 
first, last = name.split(" ")

#Returning input from the user with greeting
print(f"\nHi, {first} !") #format string


'''
#Parameters

# Print "hello, " with "??" at the end instead of a newline
print("hello, ", end="??")

# Attempt to set separator to "??", but ineffective with single argument
print("hello, ", sep="??")
'''



