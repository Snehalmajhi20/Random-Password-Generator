import random
import string

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    password_length = int(input("Enter the password length:\n"))
    password_count = int(input("Enter the number of req. passwords:\n"))
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))
    # print(s)
    while(True):
        for i in range(0, password_count):
            password = ""
            for j in range(0, password_length):
                random.shuffle(s)
                password += random.choice(s)
            print(password)
        repeat = input("Do you want generate the password again? ")
        if repeat == "no"  or repeat == "yes":
            break
print("Thank you!!")
