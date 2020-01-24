class Queue:

    def __init__(self):
        self.queue = []
    
    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        if self.size()>0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack:
    def __init__(self):
        self.queue = []

    def push(self, value):
        self.queue.append(value)

    def pop(self):
        if self.size()>0:
            return self.queue.pop()
        else:
            return None

    def size(self):
        return len(self.queue)



class RoomGraph:
    def __init__(self):
        self.rooms = {}
        self.connections = {}
        self.directions = {}
    
    def add_room(self, room):
        self.rooms[room.id] = room

    def add_connection(self, room_id, connections):
        self.connections[room_id] = list(connections.values())
        self.directions[room_id] = connections

    def get_directions(self, path):
        directions = []
        for i in range(len(path)-1):
            next_room = path[i+1]
            connected_rooms = self.directions[path[i]]
            keys = list(connected_rooms.keys())
            values = list(connected_rooms.values())
            directions.append(keys[values.index(next_room)])

        return directions



    # """
    # Return a list containing the shortest path from
    # starting_vertex to destination_vertex in
    # breath-first order.
    # """
    def bfs(self, starting_vertex, destination_vertex):

        queue = Queue()
        queue.enqueue([starting_vertex])
        visited = set()
        while queue.size() > 0:
            path = queue.dequeue()
            vertex = path[-1]
            if vertex == destination_vertex:
                # print(f"BFS PATH: {path}")
                return path
            if vertex not in visited:
                visited.add(vertex)
                for next_vertex in self.connections[vertex]:
                    new_path = list(path)
                    new_path.append(next_vertex)
                    queue.enqueue(new_path)
    

    def traverse(self):
        stack = Stack()
        path=[]
        additional_option = Stack()
        visited = set()
        stack.push(0)
        while stack.size() > 0:
            room = stack.pop()
            #print("ROOM", room)

            if room not in visited:
                #print("2. room not in visited")
                visited.add(room)
                path.append(room)
            if len(visited) == len(self.rooms):
                return path
            potential_rooms = self.connections[room]
            #print("Path: ", path)
            potential_rooms.sort()
            #print("potential_rooms: ", potential_rooms)
            # go_back = True
            possible_directions = 0
            for next_room in potential_rooms:
                if next_room not in visited:
                    #print(next_room)
                    # new_visited = set(visited)
                    # go_back = False
                    possible_directions +=1
                    stack.push(next_room)
            if possible_directions > 1:
                additional_option.push(room)
            if possible_directions == 0:
                next_room = additional_option.pop()
                #print(f"Room: {room}, Next Room: {next_room}")
                path_to_room = self.bfs(room, next_room)
                path.extend(path_to_room[1:])
                for item in path_to_room:
                    if item not in visited:
                        visited.add(item)
                stack.push(path[-1])









                    # path.append(next_room)
                    # queue.enqueue(path)
            # if go_back ==True:
            #     reverse.enqueue(path)
            #     print("REVERSE", reverse.queue)
            # # else:
            # #     print("VISITED ALREADY PATH", path)
            # while reverse.size()>0:
            #         print("1. reverse")
            #         path = reverse.dequeue()
            #         # if len(path) > 7:
            #         #     break
            #         break
            #         print("Path", path)
            #         previous_room = path[i]
            #         potential_rooms = self.connections[previous_room]
            #         potential_rooms.sort()
            #         go_back=True
            #         for next_room in potential_rooms:
            #             print("2. for next_room in reverse--next_room", next_room)

            #             if next_room not in visited:
            #                 print("3. next_room not in visited")
            #                 go_back = False
            #                 new_path = list(path)
            #                 new_path.append(previous_room)
            #                 new_path.append(next_room)
            #                 print("new_path", new_path)
            #                 queue.enqueue(new_path)
            #         if go_back == True:
            #             print("3. reverse again")
            #             i-=1
            #             new_path = list(path)
            #             new_path.append(previous_room)
            #             new_path.append(path[i])
            #             print("new_path", new_path)
            #             reverse.enqueue(new_path)

        print("Path to return: ", path)
        return path











    # def dft_traverse(self):
    #     stack = Stack()
    #     reverse = Stack()
    #     directions = []
    #     #stack is room_ids
    #     stack.push([[0], directions])
    #     visited = set()
    #     opposite_directions = {"n": "s", "s": "n", "e": "w", "w":"e"}

    #     while stack.size() > 0 :
    #         rooms_and_directions = stack.pop()
    #         rooms = rooms_and_directions[0]
    #         print("1. rooms and directions", rooms_and_directions)
    #         room_id = rooms[-1]
    #         directions = rooms_and_directions[1]
    #         if room_id not in visited:
    #             visited.add(room_id)
    #         print("room connections", self.connections[room_id])
    #         # connected_rooms = self.connections[room_id].values()
    #         # print("connected_rooms", connected_rooms.dict_values)
            
    #         # go north if possible and room not visited
    #         if "n" in self.connections[room_id]:
    #             print("if N")
    #             if self.connections[room_id]["n"] not in visited:
    #                 print("going north")
    #                 new_rooms = list(rooms)
    #                 new_rooms.append(self.connections[room_id]["n"])
    #                 new_directions = list(directions)
    #                 new_directions.append("n")
    #                 stack.push([new_rooms, new_directions])
    #                 continue
    #         # go east if possible and room not visited
    #         elif "e" in self.connections[room_id]:
    #             print("if east")
    #             if self.connections[room_id]["e"] not in visited:
    #                 print("going east")
    #                 new_rooms = list(rooms)
    #                 new_rooms.append(self.connections[room_id]["e"])
    #                 new_directions = list(directions)
    #                 new_directions.append("e")
    #                 stack.push([new_rooms, new_directions])
    #                 continue
    #         #go south if possible and room not visited
    #         elif "s" in self.connections[room_id]:
    #             print("if s")
    #             if self.connections[room_id]["s"] not in visited:
    #                 print("going south")
    #                 new_rooms = list(rooms)
    #                 new_rooms.append(self.connections[room_id]["s"])
    #                 new_directions = list(directions)
    #                 new_directions.append("s")
    #                 stack.push([new_rooms, new_directions])
    #                 continue
    #         # go west if possible and room not visited
    #         elif "w" in self.connections[room_id]:
    #             print("if w")
    #             if self.connections[room_id]["w"] not in visited:
    #                 print("going west")
    #                 new_rooms = list(rooms)
    #                 new_rooms.append(self.connections[room_id]["w"])
    #                 new_directions = list(directions)
    #                 new_directions.append("w")
    #                 stack.push([new_rooms, new_directions])
    #                 continue
    #         else:
    #             print("else go back")
    #             reverse.push([rooms, directions] )
    #             print(f"possible rooms: ")
    #             # while reverse.size > 0:
    #             #     rooms_and_directions = reverse.pop()
    #             #     rooms = rooms_and_directions[0]
    #             #     directions = rooms_and_directions[1]






    #             new_rooms = list(rooms)
    #             new_rooms.append(rooms[-2])
    #             new_directions = list(directions)
    #             back_direction = opposite_directions[directions[-1]]
    #             new_direction.append(back_direction)
    #             stack.push([new_rooms], new_direction)
                
    #     return directions

            #     new_directions.append("n")
            # if "s" in self.connections[room_id]:
            #     new_directions.append("s")
            # if "e" in self.connections[room_id]:
            #     new_directions.append("e")
            # if "w" in self.connections[room_id]:
            #     new_directions.append("w")




