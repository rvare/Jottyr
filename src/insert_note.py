import datetime
import os

def insert_note(note_content: str) -> None:
    """
    Insert new note content to the notes.txt file.
    note_content (invariant): String that contains the users note content.
    """
    iso_date = datetime.datetime.now().strftime("%Y-%m-%d")
    with open("../notes.txt", 'a', encoding="utf-8", newline='\n') as notes_file:
        notes_file.write(f"{iso_date}  {note_content}\n")
