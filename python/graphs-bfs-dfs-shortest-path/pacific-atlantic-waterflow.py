heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
result = []

if not heights: print(result)

rows, cols = len(heights), len(heights[0])
pac, atl = set(), set()

# ALGO: DFS
def dfs(r, c, visit, prevHeight):
    # Outside the grid constraint or if in visit or the current height is less than prevHeight
    if (r < 0 or c < 0 or r == rows or c == cols) or ((r,c) in visit) or (heights[r][c] < prevHeight):
        return

    visit.add((r,c))

    # recursion checking all 4 directions
    dfs(r + 1, c, visit, heights[r][c])
    dfs(r - 1, c, visit, heights[r][c])
    dfs(r, c + 1, visit, heights[r][c])
    dfs(r, c - 1, visit, heights[r][c])

# both for loops call DFS to populate visit set

# Start DFS from Left and Right edges
for r in range(rows):
    # pac and atl are the sets we pass onto the function 
    
    # current height is heights[r][0] 
    # the previous height is also height[r][0]
    # the first two paramters is the current height because these parameters change direction
    # the current height must be greater than the previous height
    dfs(r, 0, pac, heights[r][0]) # Pacific left

    # 
    dfs(r, cols - 1, atl, heights[r][cols - 1]) # Atlantic Right

# Start DFS from top and bottom edges
for c in range(cols):
    dfs(0, c, pac, heights[0][c])
    dfs(rows - 1, c, atl, heights[rows - 1][c])

for r in range(rows):
    for c in range(cols):
        if (r,c) in pac and (r,c) in atl:
            result.append([r,c])

print(result)