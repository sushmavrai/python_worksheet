def ask_user():
    user_input = input("Do you want to proceed? (yes/no): ")
    if user_input.lower() == "yes":
        print("Proceeding with the specific action...")
        # Add your specific action here
    else:
        print("No action taken.")

# Call the function
ask_user()


