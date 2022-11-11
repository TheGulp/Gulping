from room import Room
kitchen = Room("Kitchen")
kitchen.set_description("Bogos")
door = Room("door")
kitchen.link_room(door, "north")

dining_hall = Room("dining_hall")
kitchen = Room("kitchen") 
dining_hall.set_description("the chef") 
door.set_description("The floor")
current_room = kitchen

while True:
    print("\n")
    current_room.get_description()
    command = input("> ")
    current_room = current_room.move(command)
    
