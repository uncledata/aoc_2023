from functools import cache

with open("day12.txt", "r") as f:
    raw = f.read().splitlines()
raw = [line.replace("\n", "").split(" ") for line in raw]


@cache
def variants(text_to_check, sizes, num_checked_in_group=0):
    if not text_to_check:
        return not sizes and not num_checked_in_group
    num_sols = 0
    possible = [".", "#"] if text_to_check[0] == "?" else text_to_check[0]
    for chr in possible:
        if chr == "#":
            num_sols += variants(text_to_check[1:], sizes, num_checked_in_group + 1)
        else:
            if num_checked_in_group:
                if sizes and sizes[0] == num_checked_in_group:
                    num_sols += variants(text_to_check[1:], sizes[1:])
            else:
                num_sols += variants(text_to_check[1:], sizes)
    return num_sols


lines = [(line[0], tuple(map(int, line[1].split(",")))) for line in raw]
print(sum(variants(group, sizes) for group, sizes in lines))
print(sum(variants("?".join([group] * 5) + ".", sizes * 5) for group, sizes in lines))
