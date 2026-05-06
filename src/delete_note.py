from pathlib import Path
from constants import NOTES_PATH

def delete_note(line_number: int) -> None:
    """
    Delete a note from notes.txt file by using its line number.
    line_number: Integer parameter that has the line number of the note to delete.
    """
    line_number_count: int = 1
    note_list = None
    with open(f"{Path.home()}/{NOTES_PATH}", 'r', encoding="utf-8") as notes_file:
        note_list = notes_file.readlines()
        print(note_list)
    with open(f"{Path.home()}/{NOTES_PATH}", 'w', encoding="utf-8") as notes_file:
        for note in note_list:
            if line_number_count != line_number:
                notes_file.write(note)
            line_number_count += 1
