username = input()
password = input()

personal_password = input()

while personal_password != password:
    personal_password = input()

print(f"Welcome {username}!")

# Variant 2
# username = input()
# password = input()
#
# while True:
#     data = input()
#
#     if data == password:
#         break
#
# print(f"Welcome {username}!")
