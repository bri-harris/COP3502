from pathlib import Path

path = Path('pi_million_digits.txt')
contents = (path.read_text().replace('1415', 'hey!'))

lines = contents.splitlines()
pi_string = ''
for l in lines:
    if 'hey!' in l:
        pi_string += l.lstrip()

print(f"{pi_string[:999]}...")



