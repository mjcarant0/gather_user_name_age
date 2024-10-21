#Use dictionary to store the user's data
user_data = {}
#Use loop to ask user to input their name and age
while True: #first loop
    #Another loop if there is an error or if the user wants to retry
    while True: #second loop
        try:
            while True: #third loop for name to ensure that all characters are letters
                name = input("What's your name? ")
                
                if not name.isalpha():
                    print("Only letters are allowed. Please try again.")
                #to break third loop
                elif name.isalpha():
                    break
                
            while True:
                age = int(input("How old are you? "))
                
                if age < 0:
                    print("Age must be positive number. Please try again.")
                else:
                    break
            
            user_data[name] = {
                "name" : name,
                "age" : age
            }
            
            #Print user's information
            print("----------------------------------")
            print(f"This is your personal information")
            print(f"Name: {user_data[name]['name']}")
            print(f"Age: {user_data[name]['age']}")
            
            retry = input("Do you want to retry? Please enter YES or NO: ").upper()
            break #to break the second loop
        except:
            print("Please try again")
            
    if retry == "NO":
        #Adding conditional statement if the user wants to input another data/information
        new_user_data = input("Do you want to add a new entry? Please enter YES or NO: ").upper()
        if new_user_data == "YES":
            continue
        elif new_user_data == "NO":
            print("Your information has been stored. Thank you!")
            break
        else:
            print("Invalid. Please enter YES or NO: ")
    elif retry != "YES":
        print("Invalid")

#Print all the stored data in user_data
stored_data = user_data.values()

print("----------------------------------")
print("       All stored user data       ")
print(stored_data)

#Compare all the ages and compare it to find the oldest and youngest
oldest_user = max(user_data)
youngest_user = min(user_data)

print(f"The oldest user is: {oldest_user}")
print(f"The youngest user is: {youngest_user}")