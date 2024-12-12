#!/usr/bin/env python3
"""Tests for AoC day 9, 2024: Disk Fragmenter"""

from pathlib import Path

import pytest

from solution import parse_data, part1, part2


@pytest.fixture
def example_data() -> str:
    current_dir = Path(__file__).parent
    filename = current_dir.parent / "example.txt"
    try:
        return filename.read_text().strip()
    except FileNotFoundError:
        raise FileNotFoundError(f"Example input file not found at {filename}")


def test_parse(example_data: str) -> None:
    data = parse_data(example_data)
    assert len(str(data)) > 0


def test_part1(example_data: str) -> None:
    assert part1(example_data) == 1928


def test_part2(example_data: str) -> None:
    assert part2(example_data) == 2858