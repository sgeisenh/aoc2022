import collections
import fileinput
from itertools import islice


def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(islice(it, n), maxlen=n)
    if len(window) == n:
        yield tuple(window)
    for x in it:
        window.append(x)
        yield tuple(window)


def first_idx_of_window(text, window_size):
    for idx, window in enumerate(sliding_window(text, window_size)):
        if len(set(window)) == window_size:
            return idx + window_size


line = [line.strip() for line in fileinput.input()][0]

print(f"Part one: {first_idx_of_window(line, 4)}")
print(f"Part two: {first_idx_of_window(line, 14)}")
