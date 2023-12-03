from pathlib import Path
from time import perf_counter_ns

INPUT_NAME = "day01.txt"
INPUT_PATH = Path(__file__).parent.parent.parent / "input" / INPUT_NAME

parsed_input = None

def parse_line(line:str):
    return line

if INPUT_PATH.exists():
    with open(INPUT_PATH) as input_file:
        parsed_input = tuple(parse_line(line) for line in input_file)

def solution_one(parsed_input:tuple) -> str:
    input = open("/input.txt")
    number = ""
    numbers = 0
    for line in input:
        digits = 0
        digit_now = ""
        use_number = False
        if "one" in str(line):
            line = line.replace("one", "1")
        if "two" in line:
            line = line.replace("two", "2")
        if "three" in str(line):
            line = line.replace("three", "3")
            print("ThreeFoundLetter")
        if "four" in line:
            line = line.replace("four", "4")
        if "five" in line:
            line = line.replace("five", "5")
        if "six" in line:
            line = line.replace("six", "6")
        if "seven" in line:
            line = line.replace("seven", "7")
        if "eight" in line:
            line = line.replace("eight", "8")
        if "nine" in line:
            line = line.replace("nine", "9")
        if "ten" in line:
            line = line.replace("ten", "10")
            use_number = True

        print(line)

        numberss = ""
        for letter in line:
            if letter.isnumeric():
                digits += 1
                numberss += str(letter)
                print(letter)
                print("Digits " + str(digits))
                digit_now = letter

        if digits < 2:
            numberss += str(digit_now)

        numbers += int(numberss[0] + numberss[-1])
        print(numberss)
    print(numbers)


def solution_two(parsed_input:tuple) -> str:
    return ""

def solve_day() -> tuple[float,float,float]:
    start_time = perf_counter_ns()
    result_one = solution_one(parsed_input)
    mid_time = perf_counter_ns()
    result_two = solution_two(parsed_input)
    end_time = perf_counter_ns()
    time_one = (mid_time - start_time) / 1_000_000
    time_two = (end_time - mid_time) / 1_000_000
    time_total = (end_time - start_time) / 1_000_000
    print(f"=== Day 01 ===\n  · Part 1: {result_one}\n  · Part 2: {result_two}\n  · Time: {time_one}; {time_two}; {time_total}")
    return time_one, time_two, time_total