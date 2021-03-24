import sys
from encoder import *
from decoder import *


def driver(user_choice_num):
    if user_choice_num.strip() == "1":
        user_encode = input("Type line for encoder ")
        if encode_valid(user_encode):
            return encoder(user_encode)
        else:
            return (
                "Error: {} contains unsupported characters.\n The entered string should contain only latin "
                "letters, numbers and other characters.".format(user_encode)
            )

    elif user_choice_num.strip() == "2":
        user_decode = input("Type line for decoder ")
        if decode_valid(user_decode)[0]:
            return decoder(user_decode)
        else:
            return decode_valid(user_decode)[1]
    elif user_choice_num.strip() == "0":
        sys.exit()
    else:
        return "{} is not from the menu list.\n Please choose 1, 2 or 0.".format(
            user_choice_num
        )


user_choice_num = input(
    "Please, press 1 if you want to use encode function \n"
    "Please, press 2 if you want to use decode function \n"
    "Please, press 0 to exit.\n"
)

print(driver(user_choice_num))
