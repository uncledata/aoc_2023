from helpers import read_file_str, INPUTS_PATH, DEMO_PATH

DAY = 1
IS_PROD = True


def get_first_last_digits(inp: str) -> int:
    first_dig: int = 10
    last_dig: int = 10
    for ch in inp:
        if ch.is_digit():
            if first_dig == 10:
                first_dig = int(ch)
            last_dig = int(ch)
    return first_dig * 10 + last_dig


def adjust_line_get_digits(inp: str) -> str:
    return (
        inp.replace("one", "o1e")
        .replace("two", "t2o")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")
        .replace("zero", "z0o")
    )


if __name__ == "__main__":
    file_name = (
        DEMO_PATH.format(str(DAY)) if not IS_PROD else INPUTS_PATH.format(str(DAY))
    )
    lines = read_file_str(file_name)
    sm1 = 0
    sm2 = 0
    for line in lines:
        sm1 += get_first_last_digits(line)
        sm2 += get_first_last_digits()
