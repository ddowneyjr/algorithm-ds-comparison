from Queue import Queue

def bfs(maze, start, goal):
    open = Queue()
    open.enqueue(start)
    reachableList = []
    goalFound = False

    while open.queue.head is not None and not goalFound:

        current = open.dequeue()

        reachableList.append(current)

        if current == goal:
            goalFound = True



        else:
            for neighbor in maze[current]:

                if neighbor not in reachableList:
                    open.enqueue(neighbor)


    if goalFound == True:
        return reachableList


    else:
        return "Path Not Found"


maze = {
    '5': ['3', '9'],
    '3': ['1', '4'],
    '9': ['8'],
    '11': ['9', '1'],
    '1': [],
    '4': ['8'],
    '8': []
}

# print(bfs(maze, '5', '8'))
