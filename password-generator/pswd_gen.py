import random

def passwd_prompt():
    usr_input = input("Please enter option, or \"help\" for available options: ")

    if usr_input == "help":
        print("==========================================")
        print("=              Options menu              =")
        print("= [blank]   -> (default everything)      =")
        print("= v         -> verbose (generates group) =")
        print("= s         -> secure                    =")
        print("= l <value> -> length (default 8, max 20)=")

    # usr_input = input("$ ")

    elif usr_input == "":
        for i in range(7):
            variables = variables_list[i]
            print(variables, end="")

    elif usr_input == "v":
        count = 0
        while count <= 20:
            for i in range(7):
                variables = variables_list[i]
                print(variables, end="")
            count += 1
            print("")

    elif usr_input == "s":
        # TODO: make a separate secure list with a greater variety of capitals and symbols
        for i in range(7):
            variables = variables_list[i]
            print(variables, end="")

    elif usr_input[0] == "l":
        pass_len = (usr_input[2] + usr_input[3]) # concatenate the value entered for length
        pass_len = int(pass_len) # cast to an integer to make it an iterator
        for i in range(pass_len):
            variables = variables_list[i]
            print(variables, end="")

    print("\n")
    usr_input = input("Do you want to generate a new password? Y/N ")

    if usr_input == "Y" or usr_input == "y":
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

print("Welcome to Python Password Generator.")

passwd_prompt()
