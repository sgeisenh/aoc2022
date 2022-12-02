import fileinput
import heapq

sections = "\n".join(line.strip() for line in fileinput.input()).split("\n\n")
top_three = heapq.nlargest(
    3,
    (sum(int(food) for food in section.splitlines()) for section in sections),
)

print("Part one:", max(top_three))
print("Part two:", sum(top_three))
