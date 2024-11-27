from pathlib import Path

path = Path('paragraph.txt')
content = path.read_text().replace('bri','Brianna')

print(content)