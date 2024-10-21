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
print("----------------------------------")
print("       All stored user data       ")
for name, data in user_data.items(): #for x, y in dictionary.items()
    print(f"Name: {data['name']}, Age: {data['age']}")

#Compare all the ages and compare it to find the oldest and youngest
print("----------------------------------")
#variable for oldest user/s
oldest_name = {} 
oldest_age = None
#variable for youngest user/s
youngest_name = {} 
youngest_age = None

for name, data in user_data.items():
    age = data['age']
    
    #Compare the age of the users to find the oldest user/s
    if oldest_age is None or age > oldest_age:
        oldest_age = age
        oldest_name = {name: age}
    elif age == oldest_age:
        oldest_name[name] = age
    
    #Compare the age of the users to find the youngest user/s
    if youngest_age is None or age < youngest_age:
        youngest_age = age
        youngest_name = {name: age}
    elif age == youngest_age:
        youngest_name[name] = age
    
if oldest_name and youngest_name:
    print(f"The oldest user(s) is/are {', '.join(oldest_name)} with an age of {oldest_age}")
    print(f"The youngest user(s) is/are {', '.join(youngest_name)} with an age of {youngest_age}")