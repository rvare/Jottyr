# Copyright 2026 Richard Varela (rvare)
# Licnese: GPL v3

import os
import datetime
import constants
from pathlib import Path

def archive() -> None:
    """
    Used to archive notes.txt.
    Will create a new file with %Y%m%d prefixed to it.
    """
    notes_list = None
    with open(f"{Path.home()}/{constants.NOTES_PATH}",
                'r', encoding="utf-8") as notes_file:
        notes_list = notes_file.readlines()

    iso_date = datetime.datetime.now().strftime(constants.ISO_DATE_FILE_FORMAT)
    with open(f"{Path.home()}/archive_{iso_date}.txt",
                'w', encoding="utf-8") as archive_file:
        archive_file.writelines(notes_list);

    print(f"\nArchived saved to: {Path.home()}/archive_{iso_date}.txt")
