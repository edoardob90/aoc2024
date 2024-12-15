#!/usr/bin/env python3
"""AoC day 15, 2024: Warehouse Woes"""

import pathlib
import sys
from dataclasses import dataclass


@dataclass(frozen=True)
class Position:
    x: int
    y: int

    def __add__(self, other: "Position") -> "Position":
        return Position(self.x + other.x, self.y + other.y)


class Robot:
    def __init__(self, grid: "Grid") -> None:
        self.grid = grid
        self.pos: Position | None = None

    def move(self, direction: str) -> bool:
        if not self.pos:
            return False

        delta = self.grid.DIRECTIONS.get(direction)
        if not delta:
            return False

        new_pos = self.pos + delta
        target = self.grid[new_pos]

        if not target or target == "#":
            return False

        if target == ".":
            self.pos = new_pos
            return True
        elif target == "O":
            # Check if we can move the box
            if self.grid.can_push_boxes(new_pos, delta):
                self.grid.push_boxes(new_pos, delta)
                self.pos = new_pos
                return True

        return False


class Grid:
    DIRECTIONS = {
        "^": Position(-1, 0),
        ">": Position(0, 1),
        "v": Position(1, 0),
        "<": Position(0, -1),
    }

    def __init__(self, raw_grid: list[str]) -> None:
        self.tiles: dict[Position, str] = {}
        self.width = len(raw_grid[0])
        self.height = len(raw_grid)
        self.robot = Robot(self)
        self._parse_grid(raw_grid)

    def _parse_grid(self, raw_grid: list[str]) -> None:
        for x, row in enumerate(raw_grid):
            for y, tile in enumerate(row):
                pos = Position(x, y)
                if tile == "@":
                    self.robot.pos = pos
                    self.tiles[pos] = "."  # Robot starts on an empty tile
                elif tile in "#.O":
                    self.tiles[pos] = tile

    def __str__(self) -> str:
        if not self.tiles:
            return ""

        min_x = min(p.x for p in self.tiles)
        max_x = max(p.x for p in self.tiles)
        min_y = min(p.y for p in self.tiles)
        max_y = max(p.y for p in self.tiles)

        rows = []
        for x in range(min_x, max_x + 1):
            row = []
            for y in range(min_y, max_y + 1):
                pos = Position(x, y)
                if self.robot and self.robot.pos == pos:
                    row.append("@")
                else:
                    row.append(self.tiles.get(pos, "."))
            rows.append("".join(row))

        return "\n".join(rows)

    def __getitem__(self, pos: Position) -> str:
        return self.tiles.get(pos, ".")

    def __setitem__(self, pos: Position, tile: str) -> None:
        if tile == "@":
            raise ValueError("Cannot set robot position directly")
        self.tiles[pos] = tile

    def can_push_boxes(self, _from: Position, direction: Position) -> bool:
        _next = _from + direction
        content = self[_next]

        if content == ".":
            # Free tile, we can move here
            return True
        if content != "O":
            # Walls or something else
            return False

        return self.can_push_boxes(_next, direction)

    def push_boxes(self, _from: Position, direction: Position) -> None:
        _next = _from + direction
        if self[_next] == "O":
            self.push_boxes(_next, direction)

        self[_next] = "O"
        self[_from] = "."

    def get_gps(self, pos: Position) -> int:
        tile = self.tiles.get(pos)
        if not tile or tile != "O":
            return 0
        return pos.x * 100 + pos.y

    def sum_gps(self) -> int:
        return sum(
            (pos.x * 100 + pos.y) for pos, tile in self.tiles.items() if tile == "O"
        )


def parse_data(puzzle_input: str) -> tuple[list[str], str]:
    """Parse input data"""
    grid, moves = puzzle_input.split("\n\n")
    grid = grid.splitlines()
    moves = "".join(moves.strip().splitlines())  # Remove newlines
    return grid, moves


def part1(data: tuple[list[str], str]) -> int:
    """Solve part 1"""
    raw_grid, moves = data
    grid = Grid(raw_grid)
    for move in moves:
        grid.robot.move(move)
    return grid.sum_gps()


def part2(data: tuple[list[str], str]) -> int:
    """Solve part 2"""
    return 0


def solve(puzzle_input: str) -> tuple[int, int]:
    """Solve the puzzle for the given input"""
    data = parse_data(puzzle_input)
    return part1(data), part2(data)


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"\n{path}:")
        solutions = solve(pathlib.Path(path).read_text().strip())
        print("\n".join(str(solution) for solution in solutions))
