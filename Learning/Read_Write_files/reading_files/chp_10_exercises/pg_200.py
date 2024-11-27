from pathlib import Path
import json

path = Path('user_data.json')

if path.exists():
    user_dict = json.loads(path.read_text())
    for k, v in user_dict.items():
        print(f'{k} : {v}')

else:
    user_dict = {'first': input('FirstName: '),
                 'last': input('LastName: '),
                 'age': input('Age: '),
                 'pin': input('Pin: ')}
    path.write_text(json.dumps(user_dict))




# aof_ts = Path('aof_ts.txt')
#
# if aof_ts.exists():
#
#     content = (aof_ts.read_text().lower()
#                .replace('tom','tim'))
#
#     print(content.count('tim'))
#
#     lines = content.splitlines()
#     tim_lines = ''
#
#     for l in lines:
#         if 'tim' in l:
#             tim_lines += f'\n{l}'
#
#     print(tim_lines[:999])
#
# else:
#     aof_ts.write_text('Inject data pls!')



# try:
#     cat_path = Path('cat.txt')
#     dog_path = Path('dogs.txt')
#     cats = cat_path.read_text()
#     print(cats)
#
#     dogs = dog_path.read_text()
#     print(dogs)
# except FileNotFoundError as e:
#     print(e)
#


# while True:
#     try:
#         a = int(input('a: '))
#         b = int(input('b: '))
#         break
#     except ValueError:
#         print('\tPlease input a number!!')
#
# print('The sum is: ', a + b)
