FILE_NAME = 'inputs/day1.txt'


def read_file_str(file_name):
    with open(file_name, 'r') as f:
        lines = f.readlines()
    return lines

def day1_p1(lines):
    tmp = ""
    sum_val = 0
    for line in lines:
        for char in line:
            if char.isdigit():
                tmp = char
                break
        for char in reversed(line):
            if char.isdigit():  
                tmp = tmp + char
                break
        sum_val += int(tmp)
    print(sum_val)

def get_nums(str_val):
    nums = ""
    vals = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
    for i in range(0, len(str_val)):
        for check in list(vals.keys()):
            if str_val[i:].startswith(check):
                nums = nums + str(vals[check])
            elif str_val[i].isdigit():
                nums = nums + str_val[i]
    return(nums)
            

def day1_p2(lines):
    tmp = 0
    for line in lines:
        nums = get_nums(line)
        tmp += int(nums[0]+nums[-1])
    print(tmp)


if __name__ == '__main__':
    lines = read_file_str(FILE_NAME)
    day1_p1(lines)
    day1_p2(lines)

