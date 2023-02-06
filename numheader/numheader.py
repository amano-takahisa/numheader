#!/usr/bin/env python3


import argparse
import re


def main(**kwargs):
    code = False
    code_pattern = re.compile(r"```")
    header_pattern = re.compile(r"(#+) ")
    number_pattern = re.compile(r"(#+) *([1-9]([0-9]|\.)+)? +(.+)")
    numbers: list[int] = [0, 0, 0, 0, 0, 0, 0]
    level_above = 0
    skip = kwargs.get("skip", [])
    print(skip)
    with open(kwargs["file"], mode="r") as file:
        i = 0
        # for line in file:
        lines = file.readlines()
        for line in lines:
            # line = line.rstrip()
            if code_pattern.match(line):
                code = not code
            if not code:
                header_match = header_pattern.match(line)
                if header_match:
                    # generate header number
                    level = len(header_match.groups()[0])
                    if level in skip:
                        pass
                    else:
                        numbers[level - 1] = numbers[level - 1] + 1
                        if level < level_above:
                            numbers[level:] = [0 for _ in numbers[level:]]

                        level_above = level
                        number_str = ".".join([str(x) for x in numbers if x > 0]) + "."
                        # insert / replace header number
                        line = number_pattern.sub(f"\\1 {number_str} \\4", line)
                    lines[i] = line
            i = i + 1

    with open(kwargs["out"], mode="w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add numbers to markdown headers")

    parser.add_argument("-f", "--file", required=True, help="markdown file")
    parser.add_argument("-o", "--out", required=True, help="output file")
    parser.add_argument(
        "--skip",
        required=False,
        nargs="+",
        type=int,
        help="Headings at given levels are ignored.",
    )

    args = parser.parse_args()
    main(**vars(args))
