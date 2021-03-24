def decode_valid(binary_str):
    for i in binary_str:
        if int(i) == 0 or int(i) == 1:
            pass
        else:
            return False, "Contains character other than 0 or 1: ".format(binary_str)

    if len(binary_str) % 8 == 0:
        pass
    else:
        return False, "Input length is not supported."
    return True, "Valid input"


def decoder(binary_str):
    return "".join(
        [chr(int(binary_str[i: i + 8], 2)) for i in range(0, len(binary_str), 8)]
    )
