import fileinput
from itertools import takewhile

lines = [line.strip() for line in fileinput.input()]

current_path = []
contents = {}


def add_entry(name, entry):
    global contents
    loc = contents
    for subdir in current_path:
        if subdir not in loc:
            loc[subdir] = {}
        loc = loc[subdir]
    loc[name] = entry


def handle_command(command, rest):
    global current_path
    words = command.split()
    match words[1]:
        case "cd":
            match words[2]:
                case "/":
                    current_path = []
                case "..":
                    current_path.pop()
                case subdirectory:
                    current_path.append(subdirectory)
            return 1
        case "ls":
            results = list(takewhile(lambda line: not line.startswith("$"), rest))
            for result in results:
                pre, name = result.split()
                match pre:
                    case "dir":
                        add_entry(name, {})
                    case size:
                        size = int(size)
                        add_entry(name, size)
            return 1 + len(results)
    raise ValueError("Unknown command")


while lines:
    jmp = handle_command(lines[0], lines[1:])
    lines = lines[jmp:]


p1 = 0
sizes = []


def process_dir(dir):
    global p1
    size = 0
    for value in dir.values():
        if isinstance(value, int):
            size += value
        else:
            size += process_dir(value)
    sizes.append(size)
    if size <= 100000:
        p1 += size
    return size


root = process_dir(contents)
curr_space = 70000000 - root
to_free = 30000000 - curr_space

print(f"Part one: {p1}")
print(f"Part two: {min(size for size in sizes if size >= to_free)}")
