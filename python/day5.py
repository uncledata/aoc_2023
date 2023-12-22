import numpy as np
from tqdm import tqdm
import time
from joblib import Parallel, delayed


def get_range_of_map(lines, what_to_look):
    start_idx = -1
    end_idx = -1
    for idx, line in enumerate(lines):
        if what_to_look in line:
            start_idx = idx + 1
        elif start_idx != -1 and (line == ""):
            end_idx = idx
            break
    return lines[start_idx:end_idx]


with open("day4.txt", "r") as f:
    lines = f.readlines()
lines = [line.replace("\n", "") for line in lines]
seeds = [int(s) for s in lines[0].split(":")[1].strip().split(" ")]
# pt2
seeds_list = []
for i in range(0, len(seeds), 2):
    seeds_list.append(np.arange(seeds[i], seeds[i] + seeds[i + 1]))


lines = lines[2:] + [""]
map_list = [
    "seed-to-soil map:",
    "soil-to-fertilizer map:",
    "fertilizer-to-water map:",
    "water-to-light map:",
    "light-to-temperature map:",
    "temperature-to-humidity map:",
    "humidity-to-location map:",
]
vals = []

maps = {}
for mp in map_list:
    vals = []
    lns = get_range_of_map(lines, mp)
    for line in lns:
        dest_start, source_start, lngth = (int(i) for i in line.split(" "))
        vals.append({"dest": dest_start, "src": (source_start, source_start + lngth)})
    vals = sorted(vals, key=lambda d: d["src"])
    maps[mp] = vals


def chunkify(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


b = np.concatenate(seeds_list)
# Example: Dividing 'b' into chunks of size 10000
chunk_size = 5_000_000
chunks = list(chunkify(b, chunk_size))


def process_chunk(chunk):
    """Process a chunk of seeds."""
    return min([iterated_seeds(seed) for seed in chunk])


# Parallel processing of chunks


def iterated_seeds(seed):
    next_val = seed
    for mp in map_list:
        relevant_mp = maps[mp]
        if not (
            relevant_mp[0]["src"][0] > next_val or relevant_mp[-1]["src"][1] <= next_val
        ):
            for line in relevant_mp:
                dest_start, source_start = line["dest"], line["src"]
                if next_val >= source_start[0] and next_val < source_start[1]:
                    next_val = dest_start + (next_val - source_start[0])
                    break
    return next_val


# part1
print(min([iterated_seeds(seed) for seed in seeds]))


p2_val = []

print("start")
t = time.time()
results = Parallel(n_jobs=5)(delayed(process_chunk)(chunk) for chunk in tqdm(chunks))
print(min(results))
