import random

def passwd_prompt():
    preference = input("Enter S for secure, N for normal: ")

    if preference == "S":
        for i in range(9):
            variables = variables_list[i]
            print(variables, end="")
    elif preference == "N":
        for i in range(7):
            variables = variables_list[i]
            print(variables, end="")

    else:
        print("Invalid option")

    print("\n")
    preference = input("Do you want to generate a new password? Y/N ")

    if preference == "Y" or preference == "y":
        passwd_prompt()
    else:
        return

up_case1 = chr(random.randint(65, 90)) # generates a random uppercase number in the range of 65-90 ASCII
up_case2 = chr(random.randint(65, 90))
low_case1 = chr(random.randint(97, 122)) # generates a random lowercase number
low_case2 = chr(random.randint(97, 122))
low_case3 = chr(random.randint(97, 122))
low_case4 = chr(random.randint(97, 122))
rand_int1 = int(random.randint(48, 57)) # creates a random number
rand_int2 = int(random.randint(48, 57))
rand_punc = chr(random.randint(33, 38)) # creates a random punctuation point

variables_list = [up_case1, up_case2, low_case1, low_case2, low_case3, low_case4, rand_int1, rand_int2, rand_punc]

random.shuffle(variables_list)

passwd_prompt()
