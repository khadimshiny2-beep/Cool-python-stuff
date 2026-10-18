# import random
from random import sample


def generator(length):
    lower = "abcdefghijklmnopqrstuvwxyz"
    upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    numbers = "1234567890"
    symbols = "!@#$%^&*()-_+="
    all = lower + upper + numbers + symbols
    password = "".join(sample(all, length))
    return password


if __name__ == "__main__":
    print("=============== SUPER PASSWORD GENERATOR ===============")
    length = int(input("Password length (up to 76): "))
    print(f"Your password: {generator(length)}")

