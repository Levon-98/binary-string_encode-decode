def encode_valid(plain_str):
    if plain_str.isascii():
        return True
    else:
        return False


def encoder(plain_str):
    return "".join(format(ord(i), "08b") for i in plain_str)
