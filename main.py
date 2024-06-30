choice = input("lunch, dinner, breakfast: ")

if choice == "breakfast":
  type = input("north indian or south indian? ")
  if type == "south indian":
    food = input("idli or dosa? ")
    if food == "idli":
      print("you ordered idli")
    elif food == "dosa":
      print("you ordered paneer dosa")
    else:
      print("sorry sir we don't have this")
  elif type == "north indian":
    food = input("aaloo paratha or bread pakora? ")
    if food == "aaloo paratha":
      print("you ordered aaloo paratha")
    elif food == "bread pakora":
      print("you ordered bread pakora")
    else:
      print("sorry sir we don't have this")

elif choice == "lunch":
  type = input("veg or non-veg? ")
  if type == "veg":
    food = input("paneer kadhai or paneer butter masala? ")
    if food == "paneer kadhai":
      print("you ordered paneer kadhai")
    elif food == "paneer butter masala":
      print("you ordered paneer butter masala")
    else:
      print("sorry sir we don't have this")
  elif type == "non-veg":
    food = input("chicken kadhai or chicken butter masala? ")
    if food == "chicken kadhai":
      print("you ordered chicken kadhai")
    elif food == "chicken butter masala":
      print("you ordered chicken butter masala")
    else:
      print("sorry sir we don't have this")

elif choice == "dinner":
  type = input("veg or non-veg? ")
  if type == "veg":
    food = input("veg biryani or veg kadhai? ")
    if food == "veg biryani":
      print("you ordered veg biryani")
    elif food == "veg kadhai":
      print("you ordered veg kadhai")
    else:
      print("sorry sir we don't have this")
  elif type == "non-veg":
    food = input("chicken biryani or fish kadhai? ")
    if food == "chicken biryani":
      print("you ordered chicken biryani")
    elif food == "fish kadhai":
      print("you ordered fish kadhai")
    else:
      print("sorry sir we don't have this")
else:
  print("sorry sir we don't have this")
