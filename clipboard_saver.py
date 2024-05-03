"""
This program keeps track of the history of the clipboard and saves any new items copied. All items copied are
outputted to the console and at the end of the program, the entire clipboard history is saved to an output file.

Requires: pyperclipfix (https://pypi.org/project/pyperclipfix/)
"""
import pyperclipfix as clipboard_manager
import threading
import time
from datetime import datetime

OUTPUT_FILE = "clipboard.txt"


def main():
    time_started = datetime.now()

    print("Clipboard Saver Initiated:")
    print("Press enter to exit the program at any time.\n")

    # Start a thread that waits for the user to press enter
    exit_thread = threading.Thread(target=input)
    exit_thread.start()

    clipboard = []
    last_paste = clipboard_manager.paste()

    # Start saving every new item added to the clipboard until the user quits
    while exit_thread.is_alive():
        new_paste = clipboard_manager.paste()

        if new_paste != last_paste:
            last_paste = new_paste
            clipboard.append(new_paste.replace("\r\n", "\n"))  # Replace CRLF --> LF to avoid issues when saving
            print(f"New Paste: {datetime.now().strftime('%H:%M:%S')}\n{new_paste}")

        time.sleep(0.1)

    # Save output to a file
    with open(OUTPUT_FILE, "w") as f:
        f.write("".join(clipboard))

    print(f"Clipboard Saved Successfully to {OUTPUT_FILE}.")
    print(f"Program Runtime: {datetime.now() - time_started}")


if __name__ == "__main__":
    main()