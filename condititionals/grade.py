#Time stamp 2:16:18

# Assigns grades based on score input: A for 90+, B for 80-89, C for 70-79, D for 60-69, and F for <60.
score = int(input("Score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
