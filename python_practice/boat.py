num = int(input("Enter a number of kids: "))
if num % 4 == 0 and num == 4:
    print("1 boat")
elif num > 4:
    count = num // 4 +1
    print(count)
