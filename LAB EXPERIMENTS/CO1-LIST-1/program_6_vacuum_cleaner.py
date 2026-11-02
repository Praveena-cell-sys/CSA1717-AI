# Vacuum Cleaner problem - two rooms A and B

rooms = {"A": "Dirty", "B": "Dirty"}
location = "A"

print("Start:", rooms, "Vacuum in room", location)

step = 0
while rooms["A"] == "Dirty" or rooms["B"] == "Dirty":
    step += 1
    if rooms[location] == "Dirty":
        action = "Suck"
        rooms[location] = "Clean"
    elif location == "A":
        action = "Move Right"
        location = "B"
    else:
        action = "Move Left"
        location = "A"

    print("Step", step, ":", action, "->", rooms,
          "Vacuum in room", location)

print("Both rooms are clean")
