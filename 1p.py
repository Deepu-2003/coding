from collections import deque
bag ={
    "A" : ["B","C"],
    "B" : ["D","E"],
    "C" : ["F"],
    "D" : [],
    "E" : ["G"],
    "F" : [],
    "G" : []
}
def bfs(start, goal):
    queue = deque([start])
    visited = set()

    while queue:
        current  = queue.popleft()


        if current in visited:
            continue
        print("VISITING CURRENT NODE:", current)
        visited.add(current)

        if current == goal :
            print("REACHED GOAL")
            return

        for neighbor in bag[current]:
            if neighbor not in visited:
                queue.append(neighbor)
    print("GOAL NOT FOUND")
bfs("A", "G")    
         