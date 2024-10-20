#Use dictionary to store the user's data
user_data = {}
#Use loop to ask user to input their name and age
while True:
    #Another loop if there is an error or if the user wants to retry
    while True:
        try:
            name = input("What's your name? ")
            age = int(input("How old are you? "))
            
            user_data = {
                "name" : name,
                "age" : age
            }
            
            #Print user's information
            print("--------------------------")
            print(f"{user_data[name]['name']}'s personal information")
            print(f"Name: {user_data[name]['name']}")
            print(f"Age: {user_data[name]['age']}")
            break
        except:
            print("try again")