# Advent of Code 2024 🎄🎅

Solutions for [Advent of Code](https://adventofcode.com/) puzzles in multiple languages:

- Python
- Rust
- Wolfram Language (just for fun)

## Project Structure

```
.
├── 01/
│   ├── python/
│   │   └── solution.py
│   ├── rust/
│   │   ├── Cargo.toml
│   │   └── src/
│   │       └── main.rs
│   └── example.txt
├── 02/
│   └── ...
└── README.md
```

## Running Solutions

Naming convention: day folders have always **2 digits** (e.g., `2024/09/python`).

### Python

```bash
cd <day>/python
python solution.py input.txt  # or example.txt
```

### Rust

```bash
cd <day>/rust
cargo run -- input.txt # or example.txt
```

### Running Tests

- [ ] Python and Rust solutions include tests based on the example data.


## Implementation Notes

- Solutions aim to use standard libraries when possible
- Each solution includes tests using the example data from the puzzle
- Input files and puzzle texts are not included due to Advent of Code's copyright
