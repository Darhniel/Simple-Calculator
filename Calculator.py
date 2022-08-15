import valid


def init():
    print("Welcome. This is a simple calculator to help perform basic operations.")
    user_action = input("What operation would you like to perform. \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Modulos \n 6. Squares \n 7. Square Root \n 8. Exit \n")
    is_valid_input = valid.input_validation(user_action)

    if user_action == "1":
        addition()
    
    elif user_action == "2":
        subtraction()

    elif user_action == "3":
        multiplication()

    elif user_action == "4":
        division()
    
    elif user_action == "5":
        modulos()

    elif user_action == "6":
        square()

    elif user_action == "7":
        square_root()

    elif user_action == "8":
        exit()

    else:
        print("Invalid Input. Try Again!")
        init()

def addition():
    print("Input the two numbers you want to add...")

    num1 = input("Input the first number: \n")
    is_valid_number = valid.number_validation(num1)
    if is_valid_number:
        num1 = float(num1)
        num2 = input("Input the second number: \n")
        is_valid_number = valid.number_validation(num2)
        if is_valid_number:
            num2 = float(num2)
            print(num1 + num2)

            another_action = input("Do you want to perform another calculation? \n 1. Yes \n 2. No \n")
            is_valid_action = valid.input_validation(another_action)
            if another_action == "1":
                init()
            elif another_action == "2":
                exit()
            else:
                print("Invalid Input. Thanks for using the calculator.")
        else:
            print("This is not a number.")
            addition()
    else:
        print("This is not a number.")
        init()


def subtraction():
    print("Input the two numbers you want to subtract...")
    
    num1 = input("Input the first number: \n")
    is_valid_number = valid.number_validation(num1)
    if is_valid_number:
        num1 = float(num1)
        num2 = input("Input the second number: \n")
        is_valid_number = valid.number_validation(num2)
        if is_valid_number:
            num2 = float(num2)
            print(num1 - num2)

            another_action = input("Do you want to perform another calculation? \n 1. Yes \n 2. No \n")
            is_valid_action = valid.input_validation(another_action)
            if another_action == "1":
                init()
            elif another_action == "2":
                exit()
            else:
                print("Invalid Input. Thanks for using the calculator.")
        else:
            print("This is not a number.")
            subtraction()
    else:
        print("This is not a number.")
        init()

        
def multiplication():
    print("Input the two numbers you want to multiply...")
    
    num1 = input("Input the first number: \n")
    is_valid_number = valid.number_validation(num1)
    if is_valid_number:
        num1 = float(num1)
        num2 = input("Input the second number: \n")
        is_valid_number = valid.number_validation(num2)
        if is_valid_number:
            num2 = float(num2)
            print(num1 * num2)

            another_action = input("Do you want to perform another calculation? \n 1. Yes \n 2. No \n")
            is_valid_action = valid.input_validation(another_action)
            if another_action == "1":
                init()
            elif another_action == "2":
                exit()
            else:
                print("Invalid Input. Thanks for using the calculator.")
        else:
            print("This is not a number.")
            multiplication()
    else:
        print("This is not a number.")
        init()


def division():
    print("Input the two numbers you want to divide...")
    
    num1 = input("Input the first number: \n")
    is_valid_number = valid.number_validation(num1)
    if is_valid_number:
        num1 = float(num1)
        num2 = input("Input the second number: \n")
        is_valid_number = valid.number_validation(num2)
        if is_valid_number:
            num2 = float(num2)
            print(num1 / num2)

            another_action = input("Do you want to perform another calculation? \n 1. Yes \n 2. No \n")
            is_valid_action = valid.input_validation(another_action)
            if another_action == "1":
                init()
            elif another_action == "2":
                exit()
            else:
                print("Invalid Input. Thanks for using the calculator.")
        else:
            print("This is not a number.")
            division()
    else:
        print("This is not a number.")
        init()


def modulos():
    print("Input the two numbers you want to find their modulos...")
    
    num1 = input("Input the first number: \n")
    is_valid_number = valid.number_validation(num1)
    if is_valid_number:
        num1 = float(num1)
        num2 = input("Input the second number: \n")
        is_valid_number = valid.number_validation(num2)
        if is_valid_number:
            num2 = float(num2)
            print(num1 % num2)

            another_action = input("Do you want to perform another calculation? \n 1. Yes \n 2. No \n")
            is_valid_action = valid.input_validation(another_action)
            if another_action == "1":
                init()
            elif another_action == "2":
                exit()
            else:
                print("Invalid Input. Thanks for using the calculator.")
        else:
            print("This is not a number.")
            modulos()
    else:
        print("This is not a number.")
        init()


def square():
    print("Input the number you want to find it's square...")
    
    num1 = input("Input the number: \n")
    is_valid_number = valid.number_validation(num1)
    if is_valid_number:
        num1 = float(num1)
        print(num1 * num1)

        another_action = input("Do you want to perform another calculation? \n 1. Yes \n 2. No \n")
        is_valid_action = valid.input_validation(another_action)
        if another_action == "1":
            init()
        elif another_action == "2":
            exit()
        else:
            print("Invalid Input. Thanks for using the calculator.")
    else:
        print("This is not a number.")
        init()


def square_root():
    print("Input the number you want to find it's square root...")
    
    num1 = input("Input the number: \n")
    is_valid_number = valid.number_validation(num1)
    if is_valid_number:
        num1 = float(num1)
        print(num1 ** (1/2))

        another_action = input("Do you want to perform another calculation? \n 1. Yes \n 2. No \n")
        is_valid_action = valid.input_validation(another_action)
        if another_action == "1":
            init()
        elif another_action == "2":
            exit()
        else:
            print("Invalid Input. Thanks for using the calculator.")
    else:
        print("This is not a number.")
        init()


init()