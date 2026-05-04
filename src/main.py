import sys
import argparse
from insert_note import insert_note
from delete_note import delete_note
from regex_search import regex_search
from archival import archive

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A notes.txt utility")
    parser.add_argument("-f", "--format", type=str, nargs=1, help="Chang formatting for input.")
    parser.add_argument("-n", "--new-note", type=str, nargs=1, help="Create a new note and append it to the notes.txt file.")
    parser.add_argument("-i", "--important", type=bool, action=argparse.BooleanOptionalAction, help="Indicates if new note is important or note.")
    parser.add_argument("-s", "--search", type=str, nargs=1, help="Find notes based on regex.")
    parser.add_argument("-d", "--delete", type=int, nargs=1, help="Delete a note by providing the note's line number.")
    parser.add_argument("-a", "--archive", type=bool, action=argparse.BooleanOptionalAction, help="Archive the current contents of your notes.txt file.")

    args = parser.parse_args()

    if args.new_note:
        insert_note(args.new_note[0], args.format[0] if args.format else None, args.important)
    elif args.search:
        found_notes = regex_search(args.search[0])
        for note in found_notes:
            print(note)
    elif args.delete:
        delete_note(args.delete[0])
    elif args.archive:
        archive()
    else:
        print("ERROR: Must give parameters. Do --help to see all parameters.")
