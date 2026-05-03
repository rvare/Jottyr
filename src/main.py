import sys
import argparse
import insert_note
from delete_note import delete_note

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A notes.txt utility")
    parser.add_argument("-f", "--format", type=str, nargs=1, help="Chang formatting for input.")
    parser.add_argument("-n", "--new-note", type=str, nargs=1, help="Create a new note and append it to the notes.txt file.")
    parser.add_argument("-i", "--important", type=bool, action=argparse.BooleanOptionalAction, help="Indicates if new note is important or note.")
    parser.add_argument("-d", "--delete", type=int, nargs=1, help="Delete a note.")
    # parser.add_argument("-p", "--print-format", type=str, nargs='*', help="Print notes. Options: all, range [date1, date2], last.")
    # parser.add_argument("-s", "--search", type=str, nargs='*', help="Search for an entry.")

    args = parser.parse_args()
    print(f"args: {args}")

    if args.new_note:
        print("Insert")
        insert_note.insert_note(args.new_note[0], args.format[0], args.important)
    elif args.delete:
        print("Delete")
        delete_note(args.delete[0])
