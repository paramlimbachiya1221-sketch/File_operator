# File_operator

# Personal Journal Manager

## 📌 Project Description
The Personal Journal Manager is a simple Python-based application that allows users to create, view, search, and delete personal journal entries. It uses file handling to store journal entries permanently in a text file.

Each journal entry includes a date and time so users can keep track of their daily thoughts and experiences.

## 🎯 Features
- **Add Entry:** Create a new journal entry with a timestamp.
- **View Entries:** Display all saved journal entries.
- **Search Entries:** Search entries using a keyword or date.
- **Delete Entries:** Delete all journal entries after confirmation.
- **File Handling Demonstration:** Demonstrate Python file modes such as `r`, `w`, `a`, and `x`.
- **Error Handling:** Handle empty entries, missing files, permission errors, and other file-related errors.
- **Simple Menu:** Easy-to-use, menu-driven interface.

## 🛠️ Technologies Used
- Python 3
- File Handling
- Object-Oriented Programming (OOP)
- Exception Handling
- Regular Expressions
- `datetime` and `os` modules

## 📂 Project Structure

    Personal-Journal-Manager/
    ├── journal_manager.py
    ├── journal.txt
    └── README.md

**Note:** `journal.txt` is created automatically when the first journal entry is saved.

## ▶️ How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

       python journal_manager.py

5. Select an option from the displayed menu.

## 📖 File Handling Modes

| Mode | Description |
|---|---|
| `r` | Reads data from a file. |
| `w` | Writes data and overwrites existing content. |
| `a` | Adds data to the end of a file. |
| `x` | Creates a new file and fails if it already exists. |

## 💡 Learning Outcomes
- Understanding classes and objects in Python.
- Learning how to read and write text files.
- Working with timestamps using the `datetime` module.
- Handling exceptions with `try` and `except`.
- Searching text using regular expressions.
- Creating a menu-driven Python application.

## 🔮 Future Improvements
- Add password protection.
- Add an option to edit individual entries.
- Add categories and tags.
- Export journal entries to PDF.
- Add a graphical user interface using Tkinter.

## 👨‍💻 Author
Created as a Python project to practice file handling, object-oriented programming, and exception handling.

## 📄 License
This project is available for educational and personal learning purposes.
