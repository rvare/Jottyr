import os
import re

def regex_search(regex_str: str) -> list[str]:
    """
    Search for notes based on a regular expression (regex).
    regex_str: Raw string that represents a regex.
    Retruns a list of strings that represents a list of notes.
    """
    print(regex_str)
    found_notes = []
    with open("../notes.txt", 'r', encoding="utf-8") as notes_file:
        notes_list = notes_file.readlines()
        for note in notes_list:
            if re.search(regex_str, note):
                found_notes.append(note.rstrip())
    return found_notes
