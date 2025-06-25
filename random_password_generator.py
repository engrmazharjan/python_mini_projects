import random
import string

password_length = 24  # Length of the password
password = ""
charValues = string.ascii_letters + string.digits + string.punctuation

# List Comprehension to generate a random password
password = "".join([random.choice(charValues) for i in range(password_length)])

# Alternative method using a for loop
# for i in range(password_length):
#     password += random.choice(charValues)

print("Your random password is:", password)