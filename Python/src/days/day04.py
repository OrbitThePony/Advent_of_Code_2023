import re
from pathlib import Path
from time import perf_counter_ns

INPUT_NAME = "input4.txt"
INPUT_PATH = Path(__file__).parent.parent.parent / "input" / INPUT_NAME

def parse_line(line:str):
    return line

def parse_input(file_path = INPUT_PATH):
    parsed_input = open(file_path)
    return parsed_input

def solution_one(parsed_input:tuple) -> str:
    points = 0
    for line in parsed_input:
        print(type(line))
        line = line.split(":")[1].strip()
        print(line)
        string_one, string_two = line.split("|")[0], line.split("|")[1]
        numbers_one = re.findall(r"\d+", string_one)
        numbers_two = re.findall(r"\d+", string_two)
        print(string_one)
        print(numbers_one)
        numbers = 0
        for number in numbers_two:
            if number in numbers_one:
                print(number)
                numbers += 1
        points += 2**(numbers-1) if numbers > 0 else 0
        print(numbers)
        print(2**(numbers-1) if numbers > 0 else 0)

    return points

def solution_two(parsed_input:tuple) -> str:
    return ""

def solve_day() -> tuple[float,float,float]:
    times = [0,0,0,0]
    times[0] = perf_counter_ns()
    parsed_input = parse_input()
    times[1] = perf_counter_ns()
    result_one = solution_one(parsed_input)
    times[2] = perf_counter_ns()
    result_two = solution_two(parsed_input)
    times[3] = perf_counter_ns()

    time_parse = (times[1] - times[0]) / 1_000_000
    time_one = (times[2] - times[1]) / 1_000_000
    time_two = (times[3] - times[2]) / 1_000_000
    time_total = (times[3] - times[0]) / 1_000_000
    print(f"=== Day 04 ===\n  · Part 1: {result_one}\n  · Part 2: {result_two}\n  · Time: {time_parse}; {time_one}; {time_two}; {time_total}")
    return time_one, time_two, time_total

if __name__ == "__main__":
    solve_day()
