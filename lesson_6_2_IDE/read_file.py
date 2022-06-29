file_content = []
with open('text.txt', 'rt') as file:
    for line in file:
        file_content.append(f">> {line}")

with open('other_text.txt', 'wt') as file:
    for item in file_content:
        file.write(item)