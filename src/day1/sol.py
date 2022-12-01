import fileinput

lines = [line.strip() for line in fileinput.input()]

elves = []
curr = 0
for line in lines:
    if not line:
        elves.append(curr)
        curr = 0
    else:
        curr += int(line)

elves.append(curr)

p1 = max(elves)
print("Part one:", p1)

p2 = sum(sorted(elves, reverse=True)[:3])
print("Part two:", p2)
