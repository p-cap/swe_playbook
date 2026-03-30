# prerequisites[i] == 2 is one of Constraints
prerequisites = [[1,0]]

# 1 <= numCourses <= 2000
numCourses = 2

result = True

# 1. Build an Adjacency List
# the purpose of graph is to map key course and its corresponding prerequisites

# initialize the adj list
adj = {i : [] for i in range(numCourses)}
# add the courses and prerequisites to the adjacency list
for course, prereq in prerequisites:
    adj[course].append(prereq)

print(f'adj: {adj}')
# adj: {0: [], 1: [0]}

# 2. Initialize visited list to track????
# 0 = unvisited, 1 = visiting, 2 = visited
visit = [0] * numCourses

# 3. Create the DFS recursive function
# NOTE: crs is taken from the range(numCourses)
def dfs(crs):
    # A cycle is found only if the index is marked as 1 in visit
    if visit[crs] == 1: # 
        return False
    
    # 2 is marked in line 48 which means it passed all ifs and for loops
    if visit[crs] == 2:
        return True
    
    visit[crs] = 1 # Mark as currently visiting???

    # How does this for loop work?
    # crs = 0
    # # adj: {0: [], 1: [0]}
    # the for loop is used to iterate through the prerequisites of the course
    # if for loop encounters an empty [], it does NOT enter the for loop
    for pre in adj[crs]:
        if not dfs(pre):
            return False
    
    # marked safe because it got through the entire code
    visit[crs] = 2 
    return True


for i in range(numCourses):
    if not dfs(i):
        result = False
        break

if result:
    print('+++ All courses are valid +++')
else:
    print('--- NOT a valid class schedule ---')