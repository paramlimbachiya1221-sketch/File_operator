
import os
import re
from datetime import datetime


class JournalManager:

    def __init__(self):
        self.filename = "journal.txt"

    # Add a new journal entry
    def add_entry(self):
        try:
            entry = input("Enter your journal entry: ").strip()

            if not entry:
                print("Error: Journal entry cannot be empty.")
                return

            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            with open(self.filename, "a", encoding="utf-8") as file:
                file.write(f"[{timestamp}]\n")
                file.write(entry + "\n\n")

            print("Entry added successfully!")

        except (PermissionError, OSError) as e:
            print("Error while writing the file:", e)

    # View all journal entries
    def view_entries(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read()

            if not data.strip():
                print("No journal entries found.")
                return

            print("\nYour Journal Entries:")
            print(data)

        except FileNotFoundError:
            print("No journal file found. Please add an entry first.")

        except (PermissionError, OSError) as e:
            print("Error while reading the file:", e)

    # Search for a keyword or date
    def search_entry(self):
        keyword = input("Enter a keyword or date to search: ").strip()

        if not keyword:
            print("Error: Search value cannot be empty.")
            return

        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                data = file.read()

            if not data.strip():
                print("No journal entries found.")
                return

            # Split the journal into individual entries
            entries = re.split(
                r"(?=^\[\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\]\s*$)",
                data,
                flags=re.MULTILINE
            )

            matches = [
                entry for entry in entries
                if entry.strip() and keyword.lower() in entry.lower()
            ]

            if matches:
                print("\nMatching Entries:")
                for entry in matches:
                    print(entry.strip())
                    print("-" * 30)
            else:
                print("No entries found for:", keyword)

        except FileNotFoundError:
            print("No journal file found. Please add an entry first.")

        except (PermissionError, OSError) as e:
            print("Error while searching the file:", e)

    # Delete all journal entries
    def delete_all_entries(self):
        if not os.path.exists(self.filename):
            print("No journal entries to delete.")
            return

        confirmation = input(
            "Delete all entries? (yes/no): "
        ).strip().lower()

        if confirmation != "yes":
            print("Delete operation cancelled.")
            return

        try:
            os.remove(self.filename)
            print("All journal entries have been deleted.")

        except (PermissionError, OSError) as e:
            print("Error while deleting the file:", e)

    # Demonstrate file handling modes
    def demonstrate_file_modes(self):
        demo_file = "file_mode_demo.txt"

        print("\n--- File Handling Modes ---")

        try:
            # x mode: create a new file only
            try:
                with open(demo_file, "x", encoding="utf-8") as file:
                    file.write("Created using x mode.\n")

                print("x mode: File created successfully.")

            except FileExistsError:
                print("x mode: File already exists.")

            # w mode: overwrite file content
            with open(demo_file, "w", encoding="utf-8") as file:
                file.write("Written using w mode.\n")

            print("w mode: File written successfully.")

            # a mode: append content
            with open(demo_file, "a", encoding="utf-8") as file:
                file.write("Added using a mode.\n")

            print("a mode: Data appended successfully.")

            # r mode: read file content
            with open(demo_file, "r", encoding="utf-8") as file:
                data = file.read()

            print("r mode: File read successfully.")
            print("\nFile Content:")
            print(data)

        except (PermissionError, OSError) as e:
            print("Error during file demonstration:", e)

        finally:
            # Remove the temporary file if it exists
            try:
                if os.path.exists(demo_file):
                    os.remove(demo_file)
            except OSError as e:
                print("Could not remove demo file:", e)


# Main program
def main():
    manager = JournalManager()

    while True:
        print("\n--- WELCOME TO PERSONAL JOURNAL MANAGER ---")
        print("1. Add a New Entry")
        print("2. View All Entries")
        print("3. Search for an Entry")
        print("4. Delete All Entries")
        print("5. Demonstrate File Modes (r, w, a, x)")
        print("6. Exit")

        choice = input("Please select an option (1-6): ").strip()

        if choice == "1":
            manager.add_entry()

        elif choice == "2":
            manager.view_entries()

        elif choice == "3":
            manager.search_entry()

        elif choice == "4":
            manager.delete_all_entries()

        elif choice == "5":
            manager.demonstrate_file_modes()

        elif choice == "6":
            print("\nThank you for using Personal Journal Manager.")
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please select a number from 1 to 6.")


if __name__ == "__main__":
    main()
