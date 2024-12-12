from collections import deque

from aocd import data

def parse_map(input_map):
    return [[int(c) for c in line] for line in input_map.splitlines()]

def find_trailheads(grid):
    trailheads = []
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 0:
                trailheads.append((r, c))
    return trailheads

def find_score(grid, start):
    rows, cols = len(grid), len(grid[0])
    queue = deque([start])
    visited = set([start])
    reachable_nines = set()
    
    while queue:
        x, y = queue.popleft()
        
        # Check if this position is a height 9
        if grid[x][y] == 9:
            reachable_nines.add((x, y))
        
        # Explore neighbors
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and (nx, ny) not in visited:
                if grid[nx][ny] == grid[x][y] + 1:  # Valid uphill step
                    visited.add((nx, ny))
                    queue.append((nx, ny))
    
    return len(reachable_nines)

def calculate_total_score(input_map):
    grid = parse_map(input_map)
    trailheads = find_trailheads(grid)
    total_score = 0

    for trailhead in trailheads:
        visited = set()
        total_score += find_score(grid, trailhead)

    return total_score

def count_trails(grid, x, y, memo):
    if (x, y) in memo:
        return memo[(x, y)]

    rows, cols = len(grid), len(grid[0])
    total_trails = 0

    if grid[x][y] == 9:
        total_trails = 1
    else:
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == grid[x][y] + 1:
                    total_trails += count_trails(grid, nx, ny, memo)

    memo[(x, y)] = total_trails
    return total_trails

def calculate_total_rating(input_map):
    grid = parse_map(input_map)
    trailheads = find_trailheads(grid)
    memo = {}
    total_rating = 0

    for trailhead in trailheads:
        total_rating += count_trails(grid, trailhead[0], trailhead[1], memo)

    return total_rating

total_score = calculate_total_score(data)
total_rating = calculate_total_rating(data)

print("Part 1: Total Score of All Trailheads:", total_score) 
print("Part 2: Total Rating of All Trailheads:", total_rating)

