from Stack import Stack


def dfs(maze, start, goal):
    open = Stack()
    open.push(start)
    reachableList = []
    goalFound = False

    while open.stack.head is not None and not goalFound:

        current = open.pop()

        reachableList.append(current)


        if current == goal:
            goalFound = True



        else:
            for neighbor in maze[current]:

                if neighbor not in reachableList:

                    open.push(neighbor)

    if goalFound == True:
        return reachableList


    else:
        return "Path Not Found"

maze = {
  '5' : ['3','9'],
  '3' : ['1', '4'],
  '9' : ['8'],
  '11' : ['9', '1'],
  '1' : [],
  '4' : ['8'],
  '8' : []
}

#print(dfs(maze, '5', '8'))
