import datetime
import os

def insert_note(date_format: str, important: bool) -> None:
    """
    Insert new note content to the notes.txt file.
    note_content: String that contains the users note content.
    date_format: Used to set what datetime format to use. Options:
        'datetime' for date and time with hours and minutes.
    important: Boolean that indicates if the note has importance to it.
    """
    note_content = input("Start typing your note below. Hit ENTER once you're done.\n")
    datetime_str_format = "%Y-%m-%d"
    signifier = ""
    if date_format == "datetime":
        datetime_str_format = "%Y-%m-%dT%H:%M"

    if important == True:
        signifier = "(*) "

    iso_date = datetime.datetime.now().strftime(datetime_str_format)
    with open("../notes.txt", 'a', encoding="utf-8") as notes_file:
        notes_file.write(f"{signifier}{iso_date}  {note_content}\n")

