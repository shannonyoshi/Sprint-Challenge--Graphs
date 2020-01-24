from room import Room
from player import Player
from world import World
from room_graph import RoomGraph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)
# print("Rooms: ", world.print_rooms)
# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []

graph = RoomGraph()

for i in range(len(room_graph)):
#     print(f"ROOM {i}: {room_graph[i][1]}" )
    graph.add_room(world.rooms[i])

    graph.add_connection(i, room_graph[i][1])

# print("Rooms: ", graph.rooms)
# print("connections: ",graph.connections)
room_traversal = graph.traverse()
print("TRAVERSAL", room_traversal)
traversal_path = graph.get_directions(room_traversal)
print("DIRECTIONS", traversal_path)


# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
