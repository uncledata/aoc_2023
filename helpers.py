import requests
from dotenv import load_dotenv
import os

INPUTS_PATH = "inputs/day{}.txt"
DEMO_PATH = "inputs/day{}_demo.txt"


def read_file_str(file_name: str) -> list[str]:
    with open(file_name, "r") as f:
        lines = f.readlines()
    return lines


def read_file_list_separator(file_name: str, separator: str) -> list[list[str]]:
    with open(file_name, "r") as f:
        return [line.split(separator) for line in f.readlines()]


def read_file_list_separator_as_int(file_name: str, separator: str) -> list[list[int]]:
    with open(file_name, "r") as f:
        return [
            [int(str_to_int) for str_to_int in line.split(separator)]
            for line in f.readlines()
        ]


def download_input(day: str) -> None:
    load_dotenv()
    url = f"https://adventofcode.com/2023/day/{day}/input"
    input = requests.get(url, cookies={"session": os.getenv("AOC_TOKEN")}).text
    with open(f"inputs/day{day}.txt", "w") as f:
        f.write(input)
