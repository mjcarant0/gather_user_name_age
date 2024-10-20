#Use dictionary to store the user's data
user_data = {}
#Use loop to ask user to input their name and age
while True:
    #Another loop if there is an error or if the user wants to retry
    while True:
        try:
            name = input("What's your name? ")
            age = int(input("How old are you? "))
#Print user's information