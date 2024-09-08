
food = list ()
while True:
  foods = input("enter food or Quite to leave ")
  if foods == "quite"  or foods == "Quite" or foods == "leave" or foods == "Leave" or foods =="quit" or foods=="Quit":
    break
    
  food.append(foods)
print(food)
