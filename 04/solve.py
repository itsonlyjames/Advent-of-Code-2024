from aocd import data

coords = {(x, y): cell for y, row in enumerate(data.splitlines()) for x, cell in enumerate(row)}

def resolve(coordinates): return ''.join(coords.get(c, '.') for c in coordinates)
def p1(x,y): return map(resolve, zip(*[[(x+i,y), (x,y+i), (x+i,y+i), (x-i, y+i)] for i in range(4)]))
def p2(x,y): return map(resolve, zip(*[[(x-1+i,y-1+i), (x+1-i, y-1+i)] for i in range(3)]))

print(sum(sum(part in ['XMAS', 'SAMX'] for part in p1(x,y)) for x,y in coords))
print(sum(all(part in ['MAS',  'SAM' ] for part in p2(x,y)) for x,y in coords))
