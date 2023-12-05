def solution(path):
    card_array=[]
    part1_res = 0
    part2_res = 0
    with open(path,'r') as f:
        for idx, line in enumerate(f.readlines()):
            print(line.split("|"))
            numbers, winning = line.split("|")
            actual_numbers = numbers.split(":")[1].split(" ")
            winning = winning.replace("\n","").split(" ")
            match = 0
            while ("" in actual_numbers):
                actual_numbers.remove("")
            while ("" in winning):
                winning.remove("")
            for num in actual_numbers:
                if num in winning:
                    match+=1
            card_array.append((idx, 0 if match == 0 else 2**(match-1), match))
            part1_res += 0 if match == 0 else 2**(match-1)
    print(part1_res)
    print(card_array)
    copies = [1]*len(card_array)
    for idx, vals in enumerate(card_array):
        if vals[2]!=0:
            for j in range(idx+1,min(idx+1+vals[2], len(copies))):
                copies[j]=copies[j]+copies[idx]
    for i in range(0, len(copies):
        

            
solution("./day4_demo.txt")
