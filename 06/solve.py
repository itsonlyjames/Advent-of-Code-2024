from aocd import data, submit

def analyze_guard_path(grid, start_direction="up"):
    directions = {"up": (-1, 0), "right": (0, 1), "down": (1, 0), "left": (0, -1)}
    direction_order = ["up", "right", "down", "left"]
    
    # Find the initial starting position of the guard (^) in the grid
    pos = next(((i, sublist.index("^")) for i, sublist in enumerate(grid) if "^" in sublist))
    
    def run_path(grid_copy):
        current_direction = start_direction
        player_row, player_col = pos
        visited_states = set()  # Use a set to track visited states (row, col, direction)
        
        max_steps = len(grid_copy) * len(grid_copy[0]) * 4
        steps = 0
        
        while steps < max_steps:
            delta_row, delta_col = directions[current_direction]
            new_row, new_col = player_row + delta_row, player_col + delta_col
            
            # Check bounds
            if not (0 <= new_row < len(grid_copy) and 0 <= new_col < len(grid_copy[0])):
                return False
            
            # Handle wall collision: change direction
            if grid_copy[new_row][new_col] == "#":
                current_direction = direction_order[(direction_order.index(current_direction) + 1) % 4]
                continue

            # Move to the next cell
            player_row, player_col = new_row, new_col
            state = (player_row, player_col, current_direction)
            
            # Check if we've visited this state before
            if state in visited_states:
                return True
            
            visited_states.add(state)
            steps += 1
        
        return False
    
    # Track the unique positions visited
    visited_positions = set()
    current_direction = start_direction
    player_row, player_col = pos

    # Mark the starting position as visited
    visited_positions.add((player_row, player_col))

    while True:
        delta_row, delta_col = directions[current_direction]
        new_row, new_col = player_row + delta_row, player_col + delta_col

        if not (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0])):
            break

        if grid[new_row][new_col] == "#":
            current_direction = direction_order[(direction_order.index(current_direction) + 1) % 4]
            continue

        player_row, player_col = new_row, new_col
        visited_positions.add((player_row, player_col))

        if grid[new_row][new_col] in [".", "^"]:
            grid[new_row][new_col] = 'X'  # Mark the position

    # Number of unique positions visited
    unique_positions = len(visited_positions)
    
    # Loop positions that cause obstructions
    loop_positions = set()
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if (row, col) == pos or grid[row][col] == "#":
                continue
            
            # Temporarily mark this position as a wall
            grid[row][col] = "#"
            
            if run_path(grid):
                loop_positions.add((row, col))
            
            # Restore the original state of the grid
            grid[row][col] = '.'

    return {
        'unique_positions_visited': unique_positions,
        'loop_positions': loop_positions
    }

grid = [list(line) for line in data.splitlines()]

results = analyze_guard_path(grid)
print(f"Unique positions visited: {results['unique_positions_visited']}")
print(f"Loop obstruction positions: {len(results['loop_positions'])}")
print("Positions:", sorted(results['loop_positions']))

