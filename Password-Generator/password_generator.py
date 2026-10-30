# import random
from random import sample

lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
symbols = "!@#$%^&*()-_+="
all = lower + upper + numbers + symbols
len_all = len(all)

print("=============== SUPER PASSWORD GENERATOR ===============")
print(f"Select a number between 6 and {len_all}")
passwordLength = int(input("Password length: "));
if passwordLength < 6 or passwordLength > len_all:
    raise ValueError(f"The password length should be between 6 and {len_all}")
password = "".join(sample(all, passwordLength))
print(f"Your password: {password}")