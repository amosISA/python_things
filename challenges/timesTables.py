def timesTables():
    print_table((str(x * y) for x in range(1, 13)) for y in range(1, 13))

def oddTimesTables():
    print_table((str(x * y) for x in range(1, 13, 2)) for y in range(1, 13, 2))

def print_table(table):
    print('\n'.join([' '.join(row) for row in table]))

print(timesTables.__name__)
timesTables()
print('\n%s' % oddTimesTables.__name__)
oddTimesTables()