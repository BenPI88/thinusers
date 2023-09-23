import os
print("Thin Client")
auth = False
auth2 = False
while not auth:
  user = input("Username: ")
  if os.path.exists(user):
    auth = True
  else:
    print("That user doesn't exist. Please Try Again.")
dir = "~"
command = input(f"{user}@thinclient:{dir}$")
