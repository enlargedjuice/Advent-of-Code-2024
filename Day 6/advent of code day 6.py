import copy
#look at me! figured out relative file pathing :)
with open('Day 6/mapinp.txt', 'r') as file:
    samp_inp = file.read()

format = samp_inp.splitlines()
matrix = []
for item in format:
    matrix.append(list(item))
second_matrix = copy.deepcopy(matrix)

#locate the guard, return the matrix coords and then the way the guard is pointing
def find_guard(map):
    coords = []
    for item in map:
        if "^" in item:
            coords.append(map.index(item))
            coords.append(item.index("^"))
            coords.append("^")
            return coords
        elif ">" in item:
            coords.append(map.index(item))
            coords.append(item.index(">"))
            coords.append(">")
            return coords
        elif "<" in item:
            coords.append(map.index(item))
            coords.append(item.index("<"))
            coords.append("<")
            return coords
        elif "v" in item:
            coords.append(map.index(item))
            coords.append(item.index("v"))
            coords.append("v")
            return coords


#nice function to track movements
def move(map):
    on_map = True
    step_count = 0
    #index error means the guard has left the map
    while on_map == True:
        try:
            coords = find_guard(map)
            if coords[2] == "^":
                if map[coords[0]-1][coords[1]] == "." or map[coords[0]-1][coords[1]] == "X":
                    map[coords[0]][coords[1]] = "X"
                    if coords[0] - 1 >= 0:
                        map[coords[0]-1][coords[1]] = "^"
                        step_count += 1
                    else:
                        print(f"Guard has left the premises after {step_count} steps!")
                        on_map = "False"
                else:
                    map[coords[0]][coords[1]] = ">"
                    
            elif coords[2] == ">":
                if map[coords[0]][coords[1]+1] == "." or map[coords[0]][coords[1]+1] == "X":
                    map[coords[0]][coords[1]] = "X"
                    map[coords[0]][coords[1] +1] = ">"
                    step_count += 1
                else:
                    map[coords[0]][coords[1]] = "v"

            elif coords[2] == "v":
                if map[coords[0]+1][coords[1]] == "." or map[coords[0]+1][coords[1]] == "X":
                    map[coords[0]][coords[1]] = "X"
                    map[coords[0]+1][coords[1]] = "v"
                    step_count += 1  
                else:
                    map[coords[0]][coords[1]] = "<"

            elif coords[2] == "<":
                if map[coords[0]][coords[1]-1] == "." or map[coords[0]][coords[1]-1] == "X":
                    map[coords[0]][coords[1]] = "X"
                    if coords[1] - 1 >= 0:

                        map[coords[0]][coords[1] -1] = "<"
                        step_count += 1
                    else:
                        print(f"Guard has left the premises after {step_count} steps!")
                        on_map = "False"
                else:
                    map[coords[0]][coords[1]] = "^"
                
        except IndexError:
            print(f"Guard has left the premises after {step_count} steps!")
            on_map = "False"
            
    return map

comp_map = move(matrix)

move_counter = 0

for item in comp_map:
    for pos in item:
        if pos == "X" or pos == "^" or pos == "<" or pos == ">" or pos == "v":
            move_counter += 1
        else:
            continue


print(f"The guard has visited {move_counter} distinct locations.")



#part 2

def alt_move(map):
    on_map = True
    step_count = 0
    inf = False
    mmap = copy.deepcopy(map)
    leng = len(mmap)*len(mmap[1])
    #index error means the guard has left the map
    while on_map == True:
        try:
            if step_count < leng:
                coords = find_guard(mmap)
                if coords[2] == "^":
                    if mmap[coords[0]-1][coords[1]] == "." or mmap[coords[0]-1][coords[1]] == "X":
                        mmap[coords[0]][coords[1]] = "X"
                        if coords[0] - 1 >= 0:
                            mmap[coords[0]-1][coords[1]] = "^"
                            step_count += 1
                        else:
                            
                            on_map = False
                    else:
                        mmap[coords[0]][coords[1]] = ">"
                    
                elif coords[2] == ">":
                    if mmap[coords[0]][coords[1]+1] == "." or mmap[coords[0]][coords[1]+1] == "X":
                        mmap[coords[0]][coords[1]] = "X"
                        mmap[coords[0]][coords[1] +1] = ">"
                        step_count += 1
                    else:
                        mmap[coords[0]][coords[1]] = "v"

                elif coords[2] == "v":
                    if mmap[coords[0]+1][coords[1]] == "." or mmap[coords[0]+1][coords[1]] == "X":
                        mmap[coords[0]][coords[1]] = "X"
                        mmap[coords[0]+1][coords[1]] = "v"
                        step_count += 1  
                    else:
                        mmap[coords[0]][coords[1]] = "<"

                elif coords[2] == "<":
                    if mmap[coords[0]][coords[1]-1] == "." or mmap[coords[0]][coords[1]-1] == "X":
                        mmap[coords[0]][coords[1]] = "X"
                        if coords[1] - 1 >= 0:

                            mmap[coords[0]][coords[1] -1] = "<"
                            step_count += 1
                        else:
                            
                            on_map = False
                    else:
                        mmap[coords[0]][coords[1]] = "^"
            else:
                inf = True
                on_map = False
        except IndexError:
            
            on_map = False
            
    return mmap,inf

def obstacle_placer(map):
    loops = 0
    for row in map:
        indo = map.index(row)
        for item in row:
            indy = row.index(item)
            if map[indo][indy] == ".":
                map[indo][indy] = "#"
                mmap,is_inf = alt_move(map)
                if is_inf == True:
                    loops +=1
                    map[indo][indy] = "."
                else:
                    map[indo][indy] = "."
            else:
                continue
    return loops
            
print(obstacle_placer(second_matrix))




#uncomment below if you want to print the complete map
'''
fin_map = ""
for item in comp_map:
    fin_map += "".join(item)
    fin_map += "\n"

print(fin_map)
'''



