class Stack:

    def __init__(self):
        self.stack = []
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.size()>0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)



class RoomGraph:
    def __init__(self):
        self.rooms = {}
        self.connections = {}
    
    def add_room(self, room):
        self.rooms[room.id] = room
        self.connections[room.id] = {"n": "?", "s": "?", "e": "?", "w": "?"}

    def add_connection(self, room_id, connections):
        self.connections[room_id] = connections

    def dft_traverse(self):
        stack = Stack()
        reverse = Stack()
        directions = []
        #stack is room_ids
        stack.push([[0], directions])
        visited = set()
        opposite_directions = {"n": "s", "s": "n", "e": "w", "w":"e"}

        while stack.size() > 0 :
            rooms_and_directions = stack.pop()
            rooms = rooms_and_directions[0]
            print("1. rooms and directions", rooms_and_directions)
            room_id = rooms[-1]
            directions = rooms_and_directions[1]
            if room_id not in visited:
                visited.add(room_id)
            print("room connections", self.connections[room_id])
            # connected_rooms = self.connections[room_id].values()
            # print("connected_rooms", connected_rooms.dict_values)
            
            # go north if possible and room not visited
            if "n" in self.connections[room_id]:
                print("if N")
                if self.connections[room_id]["n"] not in visited:
                    print("going north")
                    new_rooms = list(rooms)
                    new_rooms.append(self.connections[room_id]["n"])
                    new_directions = list(directions)
                    new_directions.append("n")
                    stack.push([new_rooms, new_directions])
                    continue
            # go east if possible and room not visited
            elif "e" in self.connections[room_id]:
                print("if east")
                if self.connections[room_id]["e"] not in visited:
                    print("going east")
                    new_rooms = list(rooms)
                    new_rooms.append(self.connections[room_id]["e"])
                    new_directions = list(directions)
                    new_directions.append("e")
                    stack.push([new_rooms, new_directions])
                    continue
            #go south if possible and room not visited
            elif "s" in self.connections[room_id]:
                print("if s")
                if self.connections[room_id]["s"] not in visited:
                    print("going south")
                    new_rooms = list(rooms)
                    new_rooms.append(self.connections[room_id]["s"])
                    new_directions = list(directions)
                    new_directions.append("s")
                    stack.push([new_rooms, new_directions])
                    continue
            # go west if possible and room not visited
            elif "w" in self.connections[room_id]:
                print("if w")
                if self.connections[room_id]["w"] not in visited:
                    print("going west")
                    new_rooms = list(rooms)
                    new_rooms.append(self.connections[room_id]["w"])
                    new_directions = list(directions)
                    new_directions.append("w")
                    stack.push([new_rooms, new_directions])
                    continue
            else:
                print("else go back")
                reverse.push([rooms, directions] )
                print(f"possible rooms: ")
                # while reverse.size > 0:
                #     rooms_and_directions = reverse.pop()
                #     rooms = rooms_and_directions[0]
                #     directions = rooms_and_directions[1]






                new_rooms = list(rooms)
                new_rooms.append(rooms[-2])
                new_directions = list(directions)
                back_direction = opposite_directions[directions[-1]]
                new_direction.append(back_direction)
                stack.push([new_rooms], new_direction)
                
        return directions

            #     new_directions.append("n")
            # if "s" in self.connections[room_id]:
            #     new_directions.append("s")
            # if "e" in self.connections[room_id]:
            #     new_directions.append("e")
            # if "w" in self.connections[room_id]:
            #     new_directions.append("w")




