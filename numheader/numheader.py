#!/usr/bin/env python3


import argparse
import re


def main(**kwgs):
    code = False
    code_pattern = re.compile(r"```")
    header_pattern = re.compile(r"(#+) ")
    number_pattern = re.compile(r"(#+) *([1-9]([0-9]|\.)+)? +(.+)")
    sections: list[int] = [0, 0, 0, 0, 0, 0, 0]
    level_above = 0
    with open(kwgs["file"], mode="r") as file:
        i = 0
        # for line in file:
        lines = file.readlines()
        for s in lines:
            # s = line.rstrip()
            if code_pattern.match(s):
                code = not code
            if not code:
                header_match = header_pattern.match(s)
                if header_match:
                    # generate header number
                    level = len(header_match.groups()[0])
                    sections[level - 1] = sections[level - 1] + 1
                    if level < level_above:
                        sections[level:] = [0 for _ in sections[level:]]

                    level_above = level
                    section_number = ".".join([str(s) for s in sections if s > 0]) + "."
                    # insert / replace header number
                    s = number_pattern.sub(f"\\1 {section_number} \\4", s)
                    lines[i] = s
            i = i + 1

    with open(kwgs["out"], mode="w") as file:
        file.writelines(lines)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Add numbers to markdown headers")

    parser.add_argument("-f", "--file", required=True, help="markdown file")
    parser.add_argument("-o", "--out", required=True, help="output file")

    args = parser.parse_args()
    main(**vars(args))
