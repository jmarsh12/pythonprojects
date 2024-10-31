import random
import string

security_flag = False


def passwd_prompt():
    global security_flag
    usr_input = input("Please enter option, or \"help\" for available options: ")

    if usr_input == "help":
        print("===========================================")
        print("=              Options menu               =")
        print("= [blank]    -> (default everything)      =")
        print("= v          -> verbose (generates group) =")
        print("= vl <value> -> verbose with length       =")
        print("= s          -> secure                    =")
        print("= sl <value> -> secure with length        =")
        print("= l <value>  -> length (min 4, max 20)    =")
        print("===========================================")

    elif usr_input == "":
        password = generate_password(8)
        print(password)

    elif usr_input == "v":
        count = 0
        while count <= 20:
            password = generate_password(8)
            print(password)
            count += 1

    elif usr_input == "vl":
        count = 0
        pass_len = usr_input[3] + usr_input[4]
        pass_len = int(pass_len)  # cast to an integer to make it an iterator
        # try:
        #     pass_len = (usr_input[3] + usr_input[4])  # concatenate the value entered for length
        # except:
        #     print("Improper format. If desired length is < 10, enter 0 first (ie. 09)")
        #     usr_input = input("Do you want to generate a new password? Y/N ")
        #
        #     if usr_input == "Y" or usr_input == "y":
        #         passwd_prompt()
        #     else:
        #         return

        while count <= 20:

            password = generate_password(pass_len)
            print(password)
            count += 1

    elif usr_input == "s":
        security_flag = True
        password = generate_password(8)
        print(password)

    elif usr_input == "sl":
        security_flag = True
        count = 0
        while count <= 20:
            try:
                pass_len = (usr_input[2] + usr_input[3])  # concatenate the value entered for length
            except:
                print("Improper format. If desired length is < 10, enter 0 first (ie. 09)")
                usr_input = input("Do you want to generate a new password? Y/N ")

                if usr_input == "Y" or usr_input == "y":
                    passwd_prompt()
                else:
                    return

            pass_len = int(pass_len)  # cast to an integer to make it an iterator
            password = generate_password(pass_len)
            print(password)
            count += 1

    elif usr_input[0] == "l":
        try:
            pass_len = (usr_input[2] + usr_input[3])  # concatenate the value entered for length
        except:
            print("Improper format. If desired length is < 10, enter 0 first (ie. 09)")
            usr_input = input("Do you want to generate a new password? Y/N ")

            if usr_input == "Y" or usr_input == "y":
                passwd_prompt()
            else:
                return

        pass_len = int(pass_len)  # cast to an integer to make it an iterator
        password = generate_password(pass_len)
        print(password)

    security_flag = False
    print("\n")
    usr_input = input("Do you want to generate a new password? Y/N ")

    if usr_input == "Y" or usr_input == "y":
        passwd_prompt()
    else:
        return


def generate_password(length):
    global security_flag
    digits = string.digits
    u_case = string.ascii_uppercase
    l_case = string.ascii_lowercase
    spec_char = ["!", "@", "#", "$", "%", "&", "*", "?", "~", "."]

    password = [random.choice(digits), random.choice(u_case), random.choice(l_case), random.choice(spec_char)]

    if security_flag:
        for i in range(length - 3):
            random_spec = random.choice(spec_char)
            password.append(random.choice(digits + random_spec + digits + l_case + u_case + random_spec))
    else:
        for i in range(length - 3):
            random_spec = random.choice(spec_char)
            password.append(random.choice(digits + random_spec + u_case + l_case))

    random.shuffle(password)

    return ''.join(password)
