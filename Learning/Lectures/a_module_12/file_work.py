import os
# a = '../../Read_Write_files/reading_files/chp_10_exercises'
# path = os.path.join(a, 'dogs.txt')

# file = open(path, 'r')
# print(file.read())
# info = os.stat(path)
# print(info)
# os.remove('hello.txt')


path = os.path.join('/')

for dir_name, sub_dirs, files in os.walk(path):
    print(dir_name, '\tw/ subdirs:\t', sub_dirs, end=' ')
    print('& Read_Write_files:\t', files)

