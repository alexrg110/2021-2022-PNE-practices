from pathlib import Path

filename = input("File's name: ")
try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    total = 0
    for line in body:
        total += len(line)
    print(f"Total number of bases: {total}")
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
except IndexError:
    print(f"File {filename} is empty.")