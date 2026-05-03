import sys
import argparse
from insert_note import insert_note
from delete_note import delete_note

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A notes.txt utility")
    parser.add_argument("-f", "--format", type=str, nargs=1, help="Chang formatting for input.")
    parser.add_argument("-n", "--new-note", type=str, nargs=1, help="Create a new note and append it to the notes.txt file.")
    parser.add_argument("-i", "--important", type=bool, action=argparse.BooleanOptionalAction, help="Indicates if new note is important or note.")
    parser.add_argument("-d", "--delete", type=int, nargs=1, help="Delete a note.")

    args = parser.parse_args()

    if args.new_note:
        insert_note(args.new_note[0], args.format[0] if args.format else None, args.important)
    elif args.delete:
        delete_note(args.delete[0])
    else:
        print("ERROR: Must give parameters. Do --help to see all parameters.")
