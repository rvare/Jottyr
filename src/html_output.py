import os
import datetime
import constants
from pathlib import Path

def html_output() -> None:
    """
    Creates an HTML file of all notes in notes.txt.
    """
    note_lines: list = None
    signifier = ""
    with open(f"{Path.home()}/{constants.NOTES_PATH}", 'r', encoding='utf-8') as notes_file:
         note_lines = notes_file.readlines()
	
    iso_date = datetime.datetime.now().strftime(constants.ISO_DATE_FILE_FORMAT)
    with open(f"{Path.home()}/{iso_date}_notes.html", 'w', encoding='utf-8') as html_file:
        html_file.write("<!doctype html>")
        html_file.write("\n<html>")
        html_file.write("\n\t<head>")
        html_file.write("\n\t\t<meta charset=\"utf-8\">")
        html_file.write("\n\t\t<title>notes.txt</title>")
        html_file.write("\n\t</head>")
        html_file.write("\n\t<body>")
        html_file.write("\n\t\t<table>")
        html_file.write("\n\t\t\t<tr>")
        html_file.write("\n\t\t\t\t<th>Date</th>")
        html_file.write("\n\t\t\t\t<th>Content</th>")
        html_file.write("\n\t\t\t</tr>")

        for note in note_lines:
            note_date, note_content = tuple(note.split("  ", 2))
            html_file.write(f"\n\t\t\t<tr>\n\t\t\t\t<td>{note_date}</td>\n\t\t\t\t<td>{note_content.rstrip()}</td>")

        html_file.write("\n\t\t</table>")
        html_file.write("\n\t</body>")
        html_file.write("\n</html>")
