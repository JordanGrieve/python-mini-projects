from pathlib import Path

root_dir = Path(".") # Current folder
search_term = "14"

# rglob searches recursively in all files & subfolders
for path in root_dir.rglob("*"):
    if path.is_file():
        if search_term in path.stem:
            print(path.absolute())