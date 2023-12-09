from helpers import (
    read_file_list_separator_as_int,
    download_input,
    INPUTS_PATH,
    DEMO_PATH,
)

DAY = 9
IS_PROD = True


def compute(lines: list):
    seq_of_seqs = []
    for line in lines:
        seqs = []
        seqs.append(line.copy())
        cond = True
        cur_line = line.copy()
        while cond:
            seq = []
            for i in range(len(cur_line) - 1):
                seq.append(cur_line[i + 1] - cur_line[i])
            seqs.append(seq)
            cur_line = seq
            if all([v == 0 for v in seq]):
                cond = False
        seq_of_seqs.append(seqs)
    return seq_of_seqs


def day1(seq_of_seqs):
    next_val = 0
    # part1
    for cur_seq in seq_of_seqs:
        for elem in reversed(cur_seq):
            next_val += elem[-1]
    print(next_val)


def day2(seq_of_seqs):
    sm = 0
    for cur_seq in seq_of_seqs:
        next_val = 0
        prev = 0
        for elem in reversed(cur_seq):
            next_val = elem[0] - prev
            prev = next_val
        sm += next_val
    print(sm)


if __name__ == "__main__":
    file_name = (
        DEMO_PATH.format(str(DAY)) if not IS_PROD else INPUTS_PATH.format(str(DAY))
    )
    if IS_PROD:
        download_input(str(DAY))
    lines = read_file_list_separator_as_int(file_name, separator=" ")
    seq_of_seqs = compute(lines)
    day1(seq_of_seqs)
    day2(seq_of_seqs)
