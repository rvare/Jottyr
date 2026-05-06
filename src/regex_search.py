import os
import re
from pathlib import Path
from constants import NOTES_PATH

def regex_search(regex_str: str) -> list[str]:
    """
    Search for notes based on a regular expression (regex).
    regex_str: Raw string that represents a regex.
    Retruns a list of strings that represents a list of notes.
    """
    found_notes = []
    with open(f"{Path.home()}/{NOTES_PATH}", 'r', encoding="utf-8") as notes_file:
        notes_list = notes_file.readlines()
        for note in notes_list:
            if re.search(regex_str, note):
                found_notes.append(note.rstrip())
    if len(found_notes) == 0:
        raise Exception("No notes found")
    return found_notes
