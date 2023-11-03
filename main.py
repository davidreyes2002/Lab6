print("Menu\n-------------\n1. Encode\n2. Decode\n3. Quit")
number_dict = {'1': '4', '2': '5', '3': '6', '4': '7', '5': '8', '6': '9', '7': '0', '8': '1', '9': '2'}
number_dict1 = {'4': '1', '5': '2', '6': '3', '7': '4', '8': '5', '9': '6', '0': '7', '1': '8', '2': '9'}
while True:
    choice = input("Please enter an option: ")
    if choice == '1':
        password = input("Please enter your password to encode: ")
        stored = ""
        for i in range(len(str(password))):
            stored += number_dict.get(str(password)[i])
        print("Your password has been encoded and stored!")
    elif choice == '2':
        decoded = ""
        if stored != "":
            for i in range(len(stored)):
                decoded += number_dict1.get(stored[i])
            print(f"The encoded password is {stored}, and the original password is {decoded}.")
    elif choice == '3':
        break
    else:
        print("Invalid Input")