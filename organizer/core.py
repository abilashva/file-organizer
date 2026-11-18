"""Core logic: figure out where each file belongs and move it there."""
import logging
import shutil
from pathlib import Path

CATEGORIES = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp", ".svg"},
    "Documents": {".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".csv"},
    "Videos": {".mp4", ".mkv", ".mov", ".avi", ".webm"},
    "Audio": {".mp3", ".wav", ".flac", ".aac", ".m4a"},
    "Archives": {".zip", ".rar", ".7z", ".tar", ".gz"},
    "Code": {".py", ".java", ".js", ".html", ".css", ".cpp", ".c", ".json", ".sql"},
}

log = logging.getLogger("organizer")


def get_category(file: Path) -> str:
    """Return the folder name a file should go to."""
    ext = file.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return "Others"


def unique_path(dest: Path) -> Path:
    """If dest already exists, add _1, _2... so nothing gets overwritten."""
    if not dest.exists():
        return dest
    counter = 1
    while True:
        candidate = dest.with_name(f"{dest.stem}_{counter}{dest.suffix}")
        if not candidate.exists():
            return candidate
        counter += 1


def organize(folder: Path, dry_run: bool = False) -> dict:
    """Move files in `folder` into category subfolders.

    Returns a dict like {"Images": 3, "Documents": 2} with counts.
    """
    folder = Path(folder)
    if not folder.is_dir():
        raise NotADirectoryError(f"{folder} is not a folder")

    summary: dict = {}
    for item in sorted(folder.iterdir()):
        if not item.is_file() or item.name.startswith("."):
            continue  # skip subfolders and hidden files

        category = get_category(item)
        target = unique_path(folder / category / item.name)

        if dry_run:
            log.info("[DRY RUN] %s -> %s/", item.name, category)
        else:
            target.parent.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))
            log.info("Moved %s -> %s/", item.name, category)

        summary[category] = summary.get(category, 0) + 1
    return summary
