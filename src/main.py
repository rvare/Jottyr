import sys
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="A notes.txt utility")
    parser.add_argument("-f", "--format", type=str, nargs=1, help="Chang formatting for input.")
    parser.add_argument("-i", "--insert", type=str, nargs=1, help="Create a new note and append it to the notes.txt file.")
    parser.add_argument("-d", "--delete", type=str, nargs=1, help="Delete a note.")
    # parser.add_argument("-p", "--print-format", type=str, nargs='*', help="Print notes. Options: all, range [date1, date2], last.")
    # parser.add_argument("-s", "--search", type=str, nargs='*', help="Search for an entry.")

    args = parser.parse_args()
    print(f"args: {args}")

    if args.insert:
        print("Insert")
    elif args.delete:
        print("Delete")
