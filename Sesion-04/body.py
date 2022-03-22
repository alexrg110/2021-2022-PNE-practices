from pathlib import Path

filename = input("Introduce filename: ")

try:
    file_content = Path(filename).read_text()
    lines = file_content.splitlines()
    body = lines[1:]
    print(f"Body of the {filename}: ")
    for line in body:
        print(line)
except FileNotFoundError:
    print(f"{filename} does not exist.")
except IndexError:
    print(f"{filename} is empty.")
