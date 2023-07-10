def likes(names):
    count = len(names)
    if count == 0:
        print('no one likes this.')
    elif count == 1:
        print(f'{names[0]} likes this.')
    elif count == 2:
        print(f'{names[0]} and {names[1]} likes this.')
    elif count == 3:
        print(f'{names[0]}, {names[1]} and {names[2]} likes this.')
    else:
        print(f'{names[0]}, {names[1]} and {len(names) - 2} others')
    pass

likes(['Alex', 'Jacob', 'Mark', 'Max'])