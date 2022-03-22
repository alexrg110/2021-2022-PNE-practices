from pathlib import Path

filename = input("Introduce filename: ")
try:
    file_contents = Path(filename).read_text()
    lines = file_contents.splitlines()
    body = lines[1:]
    total = 0
    for line in body:
        end1 = line.replace("\n", "")
        total += len(end1)
    print(f"Total bases of {filename} is: {total}")
except FileNotFoundError:
    print(f"{filename} does not exist.")
except IndexError:
    print(f"{filename} is empty.")