
from pathlib import Path
import re

ROOT = Path(".")

# Find all NeetCode submission files
pattern = re.compile(r"submission-(\d+)(\.[^.]+)$")

for folder in ROOT.rglob("*"):
    if not folder.is_dir():
        continue

    submissions = {}

    for file in folder.iterdir():
        if not file.is_file():
            continue

        match = pattern.fullmatch(file.name)

        if match:
            index = int(match.group(1))
            extension = match.group(2)
            submissions.setdefault(extension, []).append(
                (index, file)
            )

    for extension, files in submissions.items():
        solution = folder / f"solution{extension}"

        # If a first solution already exists,
        # ignore every future submission.
        if solution.exists():
            for _, file in files:
                file.unlink()
            continue

        # Keep the earliest synced submission.
        files.sort(key=lambda item: item[0])

        _, first_file = files[0]
        first_file.rename(solution)

        # Remove all later submissions.
        for _, file in files[1:]:
            file.unlink()

print("First accepted solutions preserved.")
