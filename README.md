# File Organizer

A simple Python automation script that cleans up messy folders (like Downloads) by sorting files into folders such as `Images`, `Documents`, `Videos`, and more.

## Features
- Sorts files by extension into category folders
- `--dry-run` mode to preview changes safely
- Never overwrites files (adds `_1`, `_2`... on name clashes)
- Skips hidden files and existing subfolders
- No external dependencies (only `pytest` for tests)

## Usage
```bash
# Preview first
python main.py ~/Downloads --dry-run

# Then do it for real
python main.py ~/Downloads
```

Example output:
```
Summary:
  Documents: 4 file(s)
  Images: 7 file(s)
  Others: 1 file(s)
```

## Project structure
```
file-organizer/
├── main.py
├── organizer/
│   ├── core.py     # sorting logic
│   └── cli.py      # command line interface
├── tests/
│   └── test_core.py
├── requirements.txt
└── README.md
```

## Run tests
```bash
pip install -r requirements.txt
pytest
```

## Customize
Edit the `CATEGORIES` dictionary in `organizer/core.py` to add your own file types.

## License
MIT
