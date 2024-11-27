from pathlib import Path
import json


path = Path('username.json')
if path.exists():
    contents = path.read_text()
    u_n = json.loads(contents)
    print(f'hi {u_n}')
else:
    u_n = input('What is your name? ')
    contents = json.dumps(u_n)
    path.write_text(contents)
    print(f'{u_n}: cya later')
