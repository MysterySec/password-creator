import random
import string
import pyfiglet

ascii_text = pyfiglet.figlet_format("Password Creator", font="slant")
print(ascii_text)

print("""
-  How use ?
[
    A: "Ascii letters",
    D: "Digits",
    P: "Punctuation",
    L: "Length"
]

> A:[Boolean],D:[Boolean],P:[Boolean],L:[Int]

- Example
> A:True,D:False,P:False,L:15
> "Ujamasdbiqca"

> L:15
> "K-OV(~(G"h]q?s9X9g$g"

> A:True,P:True,L:45
> "f@<+o`=:oUXl/Rmndt".VRB#tn^izLjSX@wn,P!Eyoz@A"
""")

password_pattern = str(input("> "))
password_pattern_split = password_pattern.split(",")

password_characters = ""
password_length = 0

for i in range(len(password_pattern_split)):
    text_1 = password_pattern_split[i].split(":")

    if text_1[0] == "A":
        status = text_1[1]
        if status == "True":
            password_characters += string.ascii_letters
    elif text_1[0] == "D":
        status2 = text_1[1]
        if status2 == "True":
            password_characters += string.digits
    elif text_1[0] == "P":
        status3 = text_1[1]
        if status3 == "True":
            password_characters += string.punctuation
    elif text_1[0] == "L":
        status4 = text_1[1]
        password_length = int(status4)

if len(password_characters) < 1:
    password_characters = string.ascii_letters + string.digits + string.punctuation

if password_length < 1:
    password_length = 15

create_passsword = ''.join(random.choice(password_characters) for i in range(password_length))

print("[+] Processing...")

print("[+] Random password is:", create_passsword)