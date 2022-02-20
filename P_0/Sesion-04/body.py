from pathlib import Path

filename = input("File's name: ")
try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    print(f"Vody of the {filename} file:")
    for line in body:
        print(line)
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
except IndexError:
    print(f"File {filename} is empty.")