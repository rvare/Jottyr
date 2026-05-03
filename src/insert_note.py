import datetime
import os

def insert_note(note_content: str, date_format: str) -> None:
    """
    Insert new note content to the notes.txt file.
    note_content: String that contains the users note content.
    date_format: Used to set what datetime format to use. Options:
        'datetime' for date and time with hours and minutes.
    """
    datetime_str_format = "%Y-%m-%d"
    if date_format == "datetime":
        datetime_str_format = "%Y-%m-%dT%H:%M"

    iso_date = datetime.datetime.now().strftime(datetime_str_format)
    with open("../notes.txt", 'a', encoding="utf-8") as notes_file:
        notes_file.write(f"{iso_date}  {note_content}\n")
