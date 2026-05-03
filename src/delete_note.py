def delete_note(line_number: int) -> None:
    """
    Deletes note from notes.txt file.
    line_number: Integer parameter that has the line number of the note to delete.
    """
    line_number_count = 1
    note_lines = None
    with open("../notes.txt", 'r', encoding="utf-8") as notes_file:
        note_lines = notes_file.readlines()
        print(note_lines)
    with open("../notes.txt", 'w', encoding="utf-8") as notes_file:
        for note_line in note_lines:
            if line_number_count != line_number:
                notes_file.write(note_line)
            line_number_count += 1
