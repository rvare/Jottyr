import sys
import argparse
import re
from new_note import new_note
from delete_note import delete_note
from regex_search import regex_search
from archival import archive
from constants import *

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A notes.txt utility")
    parser.add_argument("-f", "--format", type=str, nargs=1,
                        help="Chang formatting for input.")
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

    args = parser.parse_args()

    if args.new_note:
        new_note(args.format[0] if args.format else None, args.important)
    elif args.search:
        try:
            found_notes = regex_search(args.search[0])
            for note in found_notes:
                print(note)
        except re.error:
            print(f"ERROR: The regex {args.search[0]} is not valid")
            print(f"Common Error: you're escaping sequences, "
                    + "you need to use double backslashes.")
            print("Else, review Python regex syntax.")
        except Exception as exception:
            print(exception)
    elif args.delete:
        delete_note(args.delete[0])
    elif args.archive:
        archive()
    else:
        print("ERROR: Must give parameters. Do --help to see all parameters.")

