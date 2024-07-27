num = 0
def number_checker(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

print(number_checker(0)) # Expected output: Positive