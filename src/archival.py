import os
import datetime
from pathlib import Path
from  constants import *

def archive() -> None:
    """
    Used to archive notes.txt.
    Will create a new file with %Y%m%d prefixed to it.
    """
    notes_list = None
    with open("../notes.txt", 'r', encoding="utf-8") as notes_file:
        notes_list = notes_file.readlines()

    iso_date = datetime.datetime.now().strftime("%Y%m%d")
    with open(f"{Path.home()}/archive_{iso_date}.txt", 'w', encoding="utf-8") as archive_file:
        archive_file.writelines(notes_list);
