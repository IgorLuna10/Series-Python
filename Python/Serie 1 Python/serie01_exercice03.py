try:  
    age = int(input("Enter your age: "))

    if age < 12: 
        print("Your tarif is 5 euros.")

    elif 12 <= age < 17:
        print("Your tarif is 6 euros.")

    elif 18 <= age < 26:
        print("Your tarif is 9 euros.")

    elif age >= 26 and age < 110:
        print("Your tarif is 10 euros.")

    else:
        print("Your age seems invalid.")

except ValueError:
    print("Please enter a valid number for your age.")
