def input_validation(input):
    if input:
        try:
            int(input)
            return True
        except:
            print("Your input must be a number!")
            return False
    else:
        print("Input field can't be left empty!")
        return False

def number_validation(number):
    if input:
        try:
            float(number)
            return True
        except:
            print("Your input must be a number!")
            return False
    else:
        print("Input field can't be left empty!")
        return False