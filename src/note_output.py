# Copyright 2026 Richard Varela (rvare)
# Licnese: GPL v3

import os
import datetime
import csv
import constants
from pathlib import Path

def note_output(output_format: str) -> None:
    """
    Function used to determine what output format to use.
    output_format: String that's used to determine output format type.
    """
    match output_format:
        case "html":
            html_output()
            print("html")
        case "csv":
            delimiter_output(output_format)
            print("csv")
        case "tsv":
            delimiter_output("tsv")
            print("tsv")

def _create_notes_list() -> list[str]:
    """
    Helper function for delimiter_output.
    Opens the notes.txt file and loads in all notes into a list for easy procssing.
    """
    note_lines = None
    with open(f"{Path.home()}/{constants.NOTES_PATH}", 'r', encoding='utf-8') as notes_file:
        note_lines = notes_file.readlines()
    return note_lines
            
def delimiter_output(delimiter_type: str) -> None:
    """
    Used to convert notes.txt to a delimiter format.
    This includes CSV and TSV formats.
    delimiter_type: A string used to determine what delimiter filetype to use.
    """
    note_lines: list = _create_notes_list()
    siginifer: str = ""
    delimiter_char: str = None
    iso_date: str = datetime.datetime.now().strftime(constants.ISO_DATE_FILE_FORMAT)
    field_names = ["Important", "Date", "Content"]

    if delimiter_type == "csv":
        delimiter_char = constants.COMMA_DELIMITER
    elif delimiter_type == "tsv":
        delimiter_char = constants.TAB_DELIMITER
    
    with open(f"{Path.home()}/{iso_date}_notes.{delimiter_type}", 'w', encoding='utf-8',
              newline='') as delimited_file:
        delimited_file_writer = csv.writer(delimited_file,
                                           delimiter=delimiter_char, lineterminator='\n')
        delimited_file_writer.writerow(field_names)
        
        for note in note_lines:
            split_line = note.split("  ", 2)
            split_line[1] = split_line[1].rstrip()
            
            if constants.NOTE_SIGNIFIER in split_line[0]:
                sub_split = split_line[0].split(" ")
                split_line[0] = sub_split[1]
                split_line.insert(0, sub_split[0])
            else:
                split_line.insert(0, "")
            delimited_file_writer.writerow(split_line)

        print(f"\n{delimiter_type.upper()} file saved to: {Path.home()}/{iso_date}_notes."
              + f"{delimiter_type}")

def html_output() -> None:
    """Creates an HTML file of all notes in notes.txt."""
    note_lines: list = None
    signifier: str = ""
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

    print(f"\nHTML file saved to: {Path.home()}/{iso_date}_notes.html")

