from pathlib import  Path

path = Path('programming.txt')
msg = ''

while True:
    user_in = input('names?')
    if len(msg) > 30 or user_in == 'q':
        break
    msg += f'{user_in} added... \n'

path.write_text(msg)