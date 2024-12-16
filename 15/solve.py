from aocd import data

data = data.strip('\n').split('\n')

def solve_part1(data):
    box, insts = '\n'.join(data).split('\n\n')
    warehouse = []
    robot_start = None
    for i, line in enumerate(box.split('\n')):
        row = []
        for j, c in enumerate(line):
            if c == '@':
                robot_start = (i, j)
            row.append(c)
        warehouse.append(row)
    
    dir_map = {
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
    }
    
    insts = insts.replace('\n', '')
    robot_pos = robot_start
    for inst in insts:
        rx, ry = robot_pos
        dx, dy = dir_map[inst]
        nx, ny = (rx + dx, ry + dy)
        
        if warehouse[nx][ny] == '.':
            warehouse[rx][ry] = '.'
            warehouse[nx][ny] = '@'
            robot_pos = (nx, ny)
            continue
        elif warehouse[nx][ny] == '#':
            continue
        
        tx, ty = nx, ny
        while warehouse[tx][ty] == 'O':
            tx, ty = (tx + dx, ty + dy)
        
        if warehouse[tx][ty] == '#':
            continue
        
        warehouse[tx][ty] = 'O'
        warehouse[nx][ny] = '@'
        warehouse[rx][ry] = '.'
        robot_pos = (nx, ny)
    
    total = 0
    for i, line in enumerate(warehouse):
        for j, c in enumerate(line):
            if c != 'O':
                continue
            total += 100 * i + j
    return total

def solve_part2(data):
    box, insts = '\n'.join(data).split('\n\n')
    
    expand_map = {
        '#': '##',
        'O': '[]',
        '.': '..',
        '@': '@.',
    }
    
    warehouse = []
    robot_start = None
    for i, line in enumerate(box.split('\n')):
        row = []
        for j, c in enumerate(line):
            if c == '@':
                robot_start = (i, 2 * j)
            for nc in expand_map[c]:
                row.append(nc)
        warehouse.append(row)
    
    dir_map = {
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1),
        '^': (-1, 0),
    }
    
    insts = insts.replace('\n', '')
    robot_pos = robot_start
    for inst in insts:
        rx, ry = robot_pos
        dx, dy = dir_map[inst]
        nx, ny = (rx + dx, ry + dy)
        
        if warehouse[nx][ny] == '.':
            warehouse[rx][ry] = '.'
            warehouse[nx][ny] = '@'
            robot_pos = (nx, ny)
            continue
        elif warehouse[nx][ny] == '#':
            continue
        
        if dx == 0:
            tx, ty = nx, ny
            dist = 0
            while warehouse[tx][ty] in {'[', ']'}:
                dist += 1
                tx, ty = (tx + dx, ty + dy)
            
            if warehouse[tx][ty] == '#':
                continue
            
            for i in range(dist):
                warehouse[tx][ty] = warehouse[tx - dx][ty - dy]
                tx, ty = (tx - dx, ty - dy)
            
            warehouse[nx][ny] = '@'
            warehouse[rx][ry] = '.'
            robot_pos = (nx, ny)
            continue
        
        to_push = [{(rx, ry)}]
        no_wall = True
        all_empty = False
        
        while no_wall and not all_empty:
            next_push = set()
            all_empty = True
            
            for cx, cy in to_push[-1]:
                if warehouse[cx][cy] == '.':
                    continue
                
                tx, ty = (cx + dx, cy + dy)
                
                if warehouse[tx][ty] != '.':
                    all_empty = False
                
                next_push.add((tx, ty))
                
                if warehouse[tx][ty] == '#':
                    no_wall = False
                    break
                elif warehouse[tx][ty] == '[':
                    next_push.add((tx, ty + 1))
                elif warehouse[tx][ty] == ']':
                    next_push.add((tx, ty - 1))
            
            to_push.append(next_push)
        
        if not no_wall:
            continue
        
        for i in range(len(to_push) - 1, 0, -1):
            for cx, cy in to_push[i]:
                fx, fy = (cx - dx, cy - dy)
                if (fx, fy) in to_push[i - 1]:
                    warehouse[cx][cy] = warehouse[fx][fy]
                else:
                    warehouse[cx][cy] = '.'
        
        warehouse[rx][ry] = '.'
        robot_pos = (nx, ny)
    
    total = 0
    for i, line in enumerate(warehouse):
        for j, c in enumerate(line):
            if c != '[':
                continue
            total += 100 * i + j
    return total

print("Part 1 Result:", solve_part1(data))
print("Part 2 Result:", solve_part2(data))
