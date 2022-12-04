import fileinput

lines = [line.strip() for line in fileinput.input()]

p1 = 0
p2 = 0
for line in lines:
    left, right = line.split(",")
    llo, lhi = map(int, left.split("-"))
    rlo, rhi = map(int, right.split("-"))
    if (llo <= rlo and lhi >= rhi) or (rlo <= llo and rhi >= lhi):
        p1 += 1
    if (llo <= rlo and lhi >= rlo) or (rlo <= llo and rhi >= llo):
        p2 += 1

print(f"Part one: {p1}")
print(f"Part two: {p2}")
