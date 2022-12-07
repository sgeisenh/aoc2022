import fileinput
from collections import defaultdict

lines = [line.strip() for line in fileinput.input()]

current_path = []
sizes = defaultdict(int)

for line in lines:
    words = line.split()
    if words[0] == "$" and words[1] == "cd":
        match words[2]:
            case "/":
                current_path = []
            case "..":
                current_path.pop()
            case sub:
                current_path.append(sub)
        continue
    try:
        size = int(words[0])
    except Exception:
        continue
    for i in range(len(current_path) + 1):
        sizes[tuple(current_path[:i])] += size

p1 = sum(size for size in sizes.values() if size <= 100000)

root = sizes[()]
capacity = 70000000
needed = 30000000
overage = root + needed - capacity
p2 = min(size for size in sizes.values() if size >= overage)

print(f"Part one: {p1}")
print(f"Part two: {p2}")
