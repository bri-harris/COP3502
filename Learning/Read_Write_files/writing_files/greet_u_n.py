from pathlib import Path
import json

path = Path('username.json')
contents = path.read_text()
u_n = json.loads(contents)

print(f'hi {u_n}')