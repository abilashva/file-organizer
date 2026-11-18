"""Command line entry point."""
import argparse
import logging
from pathlib import Path

from .core import organize


def main() -> None:
    parser = argparse.ArgumentParser(description="Sort files in a folder by type.")
    parser.add_argument("folder", type=Path, help="Folder to organize")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would happen without moving anything")
    args = parser.parse_args()

    logging.basicConfig(level=logging.INFO, format="%(message)s")
    try:
        summary = organize(args.folder, dry_run=args.dry_run)
    except NotADirectoryError as e:
        parser.error(str(e))

    if not summary:
        print("Nothing to organize.")
        return
    print("\nSummary:")
    for category, count in sorted(summary.items()):
        print(f"  {category}: {count} file(s)")


if __name__ == "__main__":
    main()
