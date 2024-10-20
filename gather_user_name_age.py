#Use dictionary to store the user's data
user_data = {}
#Use loop to ask user to input their name and age
while True: #first loop
    #Another loop if there is an error or if the user wants to retry
    while True: #second loop
        try:
            name = input("What's your name? ")
            age = int(input("How old are you? "))
            
            user_data[name] = {
                "name" : name,
                "age" : age
            }
            
            #Print user's information
            print("----------------------------------")
            print(f"This is your personal information")
            print(f"Name: {user_data[name]['name']}")
            print(f"Age: {user_data[name]['age']}")
            
            retry = input("Do you want to retry? Please enter YES or NO ").upper()
            break #to break the second loop
        except:
            print("Please try again")
            
    if retry == "NO":
        print("Your information has been stored. Thank you!")
        break
    elif retry != "YES":
        print("Invalid")