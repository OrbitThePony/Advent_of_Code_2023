from pathlib import Path
from time import perf_counter_ns
import re

INPUT_NAME = "day01.txt"
INPUT_PATH = Path(__file__).parent.parent.parent / "input" / INPUT_NAME

def parse_line(line:str):
    if len(line) == 0:
        return 
    return line

def parse_input(file_path = INPUT_PATH):
    parsed_input = list()
    if file_path.exists():
        with open(file_path) as input_file:
            parsed_input = [parse_line(line.strip()) for line in input_file]
    return tuple(x for x in parsed_input if x is not None)

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
    numbers = []
    word_values = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    number_pattern = re.compile(r'([1-9]|one|two|three|four|five|six|seven|eight|nine)')
    reverse_pattern = re.compile(r'([1-9])|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin')
    for line in parsed_input:
        first,last = number_pattern.search(line).group(),reverse_pattern.search(line[::-1]).group()
        print(first,last)
        numbers.append((word_values[first]*10)+word_values[last[::-1]])
    return str(sum(numbers))

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
    print(f"=== Day 01 ===\n  · Part 1: {result_one}\n  · Part 2: {result_two}\n  · Time: {time_parse}; {time_one}; {time_two}; {time_total}")
    return time_one, time_two, time_total

if __name__ == "__main__":
    solve_day()
