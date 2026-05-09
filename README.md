# Jottyr

A Python utility to work with notes.txt file.

(Don't know what a notes.txt file is? check out my article: [notes.txt](https://rvare.github.io/notestxt.html).

## Features

- Easily write and save notes,
- Easily delete specific notes,
- Archive your notes,
- Export your notes as a single HTML file,
- Find notes using Python regex.

## Usage

*Note:* Be sure to add this to your path with an alias of `jottyr` before you use this.

To write a new note, use the `-n` flag and hit enter:

```bash
jottyr -n
```

To delete, first find the note's line number, then use the `-d` flag with the line number to delete it:

```bash
jottyr -d <line_number>
```

You will see the output `Note saved` once you have hit enter.

To archive your notes, use the `-a` flag:

```bash
jottyr -a
```

You will see the following output once ran: `Archived saved to: <path to home>/archive_<iso_date>.txt`.
This will save a text file with all your current notes in a file of the following form: `archive_<ISO DATE>.txt`.

To export your notes as a single HTML file, use the `-o` flag:

```bash
jottyr -o
```

The HTML file will be saved in your home directory, and you will see the following output: `HTML file saved to: <path to home>/<iso_date>_notes.html

To search for a note, use a regular expression with the `-s` flag

```bash
jottyr -s <regex>
```

Output will look like the following: `<line number> <note>`

*Note:* I recommend using `grep` or `findstr` (on Windows) instead, as those programs have a much easier syntax for writing regexs with. The reason this feature is supplied with Jottyr is for convinence.

## Getting Help

Run `jottyr -h` to see all commands.

## License

See `LICENSE` for details.