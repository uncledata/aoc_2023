import json
from copy import deepcopy
with open("day19.txt", "r") as f:
    lines = f.read().splitlines()


def parse_rules(lines):
    rules = {}
    rules_list = lines[:lines.index("")]

    for rule in rules_list:
        rule_name = rule.split("{")[0]
        checks = rule.split("{")[1].split("}")[0].split(",")
        rules[rule_name] = checks
    
    return rules



def get_parts_list(lines):
    parts_list_to_parse = lines[lines.index("")+1:]
    part_list_new=[]
    for part in parts_list_to_parse:
        part = part.replace("=", '":"').replace(",", '","').replace("{", '{"').replace("}", '"}')
        part_json = json.loads(part)
        fixed_dict = {}
        for key, val in part_json.items():
            fixed_dict[key]=int(val)
        part_list_new.append(fixed_dict)
    return part_list_new

def run_checks(parts_list):
    good_parts = []
    for part in parts_list:
        workflow = 'in'
        while workflow not in ('R', 'A'):
            cur_rule = rules[workflow]
            for rule in cur_rule:
                if ":" in rule:
                    parsed_rule, pot_workflow = rule.split(":")
                    for key, val in part.items():
                        parsed_rule = parsed_rule.replace(key, str(val))
                    if eval(parsed_rule):
                        workflow = pot_workflow
                        break
                else:
                    workflow = rule
        if workflow =='A':
            good_parts.append(part)
    return good_parts
#part1
rules = parse_rules(lines)
parts_list= get_parts_list(lines)
good_parts = run_checks(parts_list)

def part1():
    sm = 0
    for part in good_parts:
        for _, val in part.items():
            sm+=val
    print(sm)

part1()

def adjust_range(rng_id, sign, limit, ranges_dict):
    ranges_dict_cp = ranges_dict.copy()
    if ranges_dict_cp[rng_id]:
        if sign == '>':
            ranges_dict_cp[rng_id] = (limit, ranges_dict[rng_id][1])
        else:
            ranges_dict_cp[rng_id] = (ranges_dict[rng_id][0], limit)
    return ranges_dict_cp

sm =0
def dfs(ranges, node):
    if node == "A":
        return (ranges['x'][1]-ranges['x'][0]+1)* (ranges['m'][1]-ranges['m'][0]+1) * (ranges['a'][1]-ranges['a'][0]+1) * (ranges['s'][1]-ranges['s'][0]+1)
    if node == "R":
        return 0
    tot = 0
    workflow_list = rules[node]
    new_ranges = deepcopy(ranges)
    for rule in workflow_list:
        if ":" in rule:
            ss = "<" if "<" in rule else ">"
            check, dest = rule.split(":")
            symbol, val = check.split(ss)
            val = int(val)
            min_s = new_ranges[symbol][0]
            max_s = new_ranges[symbol][1]
            if val >= min_s and val <= max_s:
                if ss == ">":
                    tot += dfs(adjust_range(symbol, ss, val+1, new_ranges), dest)
                    new_ranges = adjust_range(symbol, "<", val, new_ranges)
                if ss == "<":
                    tot += dfs(adjust_range(symbol, ss, val-1, new_ranges), dest)
                    new_ranges = adjust_range(symbol, ">", val, new_ranges)
        else:
            tot += dfs(new_ranges, rule)
    return tot
    
all_range = (1,4000)

ranges = {"x": all_range, "m": all_range, "a": all_range, "s": all_range}

print(dfs(ranges, "in"))
