# Copyright 2026 Richard Varela (rvare)
# Licnese: GPL v3

import sys
import argparse
import re
from new_note import new_note
from delete_note import delete_note
from regex_search import regex_search
from archival import archive
from html_output import html_output
from constants import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A notes.txt utility")
    parser.add_argument("-f", "--format", type=str, nargs=1,
                        help="Chang formatting for date format."
                        + " When not given, default to using just date."
                        + " Use 'datetime' to include both date and time.")
    parser.add_argument("-i", "--important",
                        action=argparse.BooleanOptionalAction,
                        help="Indicates if new note is important or note.")
    parser.add_argument("-n", "--new-note",
                        action=argparse.BooleanOptionalAction,
                        help="Create a new note and append it to the notes.txt file.")
    parser.add_argument("-s", "--search", type=str, nargs=1,
                        help="Find notes based on regex.")
    parser.add_argument("-d", "--delete", type=int, nargs=1,
                        help="Delete a note by providing the note's line number.")
    parser.add_argument("-a", "--archive",
                        action=argparse.BooleanOptionalAction,
                        help="Archive the current contents of your notes.txt file.")
    parser.add_argument("-o", "--output", action=argparse.BooleanOptionalAction,
                        help="Output your notes.txt file into an HMTL file.")

    args = parser.parse_args()

    try:
        if args.new_note:
            new_note(args.format[0] if args.format else None, args.important)
        elif args.search:
            found_notes = regex_search(args.search[0])
            for note in found_notes:
                print(note)
        elif args.delete:
            delete_note(args.delete[0])
        elif args.archive:
            archive()
        elif args.output:
            html_output()
        else:
            print("ERROR: Must give parameters. Do --help to see all parameters.")
    except KeyboardInterrupt as ki_ex: # For now, we'll exit when a control signal happens.
        exit()
    except re.error:
        print(f"ERROR: The regex {args.search[0]} is not valid")
        print(f"Common Error: you're escaping sequences, "
              + "you need to use double backslashes.")
        print("Else, review Python regex syntax.")
    except FileNotFoundError as file_not_found_er:
        print(file_not_found_er)
    except PermissionError as permission_er:
        print(permission_er)
    except Exception as exception:
        print(exception)
