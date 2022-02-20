from pathlib import Path

filename = input("File's name: ")
try:
    file_contents = Path(filename).read_text()
    print(file_contents)
except FileNotFoundError:
    print(f"The file {filename} does not exist.")