# Simple Vacuum Cleaner Program

rooms = {
    "A": "Dirty",
    "B": "Dirty"
}

current_room = "A"

while True:
    print("\n----------------------")
    print("Vacuum Cleaner")
    print("----------------------")

    print("Currently in room:", current_room)
    print("Room A:", rooms["A"])
    print("Room B:", rooms["B"])

    # Check if the current room is dirty
    if rooms[current_room] == "Dirty":
        print("The room is dirty. Cleaning it...")
        rooms[current_room] = "Clean"
        print("Room", current_room, "is now clean.")

    else:
        print("The room is already clean.")

    # Check if both rooms are clean
    if rooms["A"] == "Clean" and rooms["B"] == "Clean":
        print("\nBoth rooms are clean!")
        print("Vacuum cleaner has finished its work.")
        break

    # Move to the other room
    if current_room == "A":
        current_room = "B"
    else:
        current_room = "A"
