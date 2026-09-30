"""Check the output directory before replacing generated files."""
import re

def check_folder(FOLDER):
    FOLDER.mkdir(exist_ok=True)
    for file in FOLDER.iterdir():
        if file.is_symlink() or not file.is_file():
            raise ValueError("Split contains an unexpected item. Move your personal files elsewhere first.")
        if file.name != "summary.txt" and not re.fullmatch(r"person_[0-9]+\.png", file.name):
            raise ValueError("Split contains an unrelated file. Move it elsewhere before generating a new split.")


