def age_group_classifier(age):

    if age <= 12:
        print("Child")
    elif age > 12 and age < 19:
        print("Teenager")
    elif age > 19 and age < 64:
        print("Adult")
    elif age > 64:
        print("Senior")
    else:
        print("Invalid age")

# Test cases
age_group_classifier(67) # should print Senior