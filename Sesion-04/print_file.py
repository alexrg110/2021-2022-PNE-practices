from pathlib import Path

filename = input("Enter a filename: ")

try:
    file_name = Path(filename).read_text()
    print(file_name)
except FileNotFoundError:
    print("File does not exist.")