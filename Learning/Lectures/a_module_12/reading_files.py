# file = open('data.txt')

# contents = file.readlines()
# file.close()

# print(contents)

# for l in contents:
#     print(l.strip())

# for l in file:
#     print(l.strip())

# file.close()


# file = open('data.txt', "a")
# file.write("Hello")
# file.close()

with open('scores.txt', 'a+') as file:
    total = 0
    for line in file.readlines():
        for i in line.strip().split():
            total += int(i)
        # file.write(f'\n{total}')

            file.seek(0)
            file.write(f'\n{total}')
