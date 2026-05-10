# Copyright 2026 Richard Varela (rvare)
# Licnese: GPL v3

import datetime
import os
import constants
from pathlib import Path

def new_note(date_format: str, important: bool) -> None:
    """
    Insert new note content to the notes.txt file.
    note_content: String that contains the users note content.
    date_format: Used to set what datetime format to use. Options:
        'datetime' for date and time with hours and minutes.
    important: Boolean that indicates if the note has importance to it.
    """
    note_content = input("Start typing your note below. Hit ENTER once you're done.\n")
    datetime_str_format = constants.ISO_DATE_FORMAT
    signifier = ""
    if date_format == "datetime":
        datetime_str_format = constants.ISO_DATETIME_FORMAT

    if important == True:
        signifier = constants.NOTE_SIGNIFIER

    iso_date = datetime.datetime.now().strftime(datetime_str_format)
    with open(f"{Path.home()}/{constants.NOTES_PATH}", 'a',
                encoding="utf-8") as notes_file:
        notes_file.write(f"{signifier}{iso_date}  {note_content}\n")

    print("\nNote saved.")
