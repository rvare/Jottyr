# Copyright 2026 Richard Varela (rvare)
# Licnese: GPL v3

from pathlib import Path
from constants import NOTES_PATH

def delete_note(line_number: int) -> None:
    """
    Delete a note from notes.txt file by using its line number.
    Displays the note that was deleted.
    line_number: Integer parameter that has the line number of the note to delete.
    """
    line_number_count: int = 1
    note_list: list = None
    deleted_note: str = None
    with open(f"{Path.home()}/{NOTES_PATH}", 'r', encoding="utf-8") as notes_file:
        note_list = notes_file.readlines()

    with open(f"{Path.home()}/{NOTES_PATH}", 'w', encoding="utf-8") as notes_file:
        for note in note_list:
            if line_number_count != line_number:
                notes_file.write(note)
            else:
                deleted_note = note
            line_number_count += 1

    print(f"\nNote deleted: {note}")
