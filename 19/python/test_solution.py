#!/usr/bin/env python3
"""Tests for AoC day 19, 2024: Linen Layout"""

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
    assert len(data) > 0


def test_part1(example_data: str) -> None:
    trie, designs = parse_data(example_data)
    assert part1(trie, designs) == 6


def test_part2(example_data: str) -> None:
    trie, designs = parse_data(example_data)
    assert part2(trie, designs) == 16
