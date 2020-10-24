import re

test = "Hello World!"
test2 = "12345"

print("Good 0") if re.search("[a-z]", test) else print("Bad 0")
print("Good 1") if re.search("[0-9]", test2) else print("Bad 1")
print("Bad 2") if re.search("[0-9]", test) else print("Good 2")
print("Bad 3")if re.search("[a-z]", test2)else print("Good 3")
