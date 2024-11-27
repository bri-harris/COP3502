from pathlib import Path

path = Path('pi_million_digits.txt')
contents = path.read_text()

lines = contents.splitlines()
pi_string = ''
for l in lines:
    pi_string += l.lstrip()

bday = input('Input bday:')
if bday in pi_string:
    print(f'{bday} ∃ in pi!')
else:
    print(f'{bday} !∃')
