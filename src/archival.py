import os
import datetime

def archive() -> None:
    """Used to archive notes.txt."""
    notes_list = None
    with open("../notes.txt", 'r', encoding="utf-8") as notes_file:
        notes_list = notes_file.readlines()

    iso_date = datetime.datetime.now().strftime("%Y%m%d")
    with open(f"../archive_{iso_date}.txt", 'w', encoding="utf-8") as archive_file:
        archive_file.writelines(notes_list);
