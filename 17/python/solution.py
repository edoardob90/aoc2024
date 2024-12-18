#!/usr/bin/env python3
"""AoC day 17, 2024: Chronospatial Computer"""

import pathlib
import sys

from utils import ilist


def parse_data(puzzle_input: str) -> tuple[list[int], int, int, int]:
    """Parse input data"""
    regs, prog = puzzle_input.split("\n\n")
    a, b, c = tuple(int(line.split(":", 1)[-1]) for line in regs.splitlines())
    return ilist(prog.split(":")[-1], ","), a, b, c


def part1(
    prog: list[int], a: int, b: int, c: int, print_prog: bool = False
) -> list[int]:
    """Solve part 1"""
    if print_prog:
        print(
            f"Register A: {a}\nRegister B: {b}\nRegister C: {c}\n\nProgram: {','.join(str(x) for x in prog)}\n"
        )
    ip, out = 0, []
    while ip < len(prog):
        instr, operand = prog[ip], prog[ip + 1]
        combo = operand, operand, operand, operand, a, b, c
        a = a // (2 ** combo[operand]) if instr == 0 else a
        b = b ^ operand if instr == 1 else b
        b = combo[operand] % 8 if instr == 2 else b
        ip = operand - 2 if instr == 3 and a != 0 else ip
        b = b ^ c if instr == 4 else b
        if instr == 5:
            out.append(combo[operand] % 8)
        b = a // (2 ** combo[operand]) if instr == 6 else b
        c = a // (2 ** combo[operand]) if instr == 7 else c
        ip += 2

    return out


def part2(prog: list[int], n: int, a: int) -> int:
    """Solve part 2"""
    if n == -1:
        return a
    a <<= 3
    for i in range(8):
        if part1(prog, a + i, 0, 0) == prog[n:]:
            s = part2(prog, n - 1, a + i)
            if s != -1:
                return s
    return -1


def solve(puzzle_input: str) -> tuple[str, int]:
    """Solve the puzzle for the given input"""
    prog, a, b, c = parse_data(puzzle_input)
    p1 = ",".join(str(x) for x in part1(prog, a, b, c, True))
    p2 = part2(prog, len(prog) - 1, 0)
    part1(prog, p2, 0, 0, True)
    return p1, p2


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
