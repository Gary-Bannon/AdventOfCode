import itertools
file1 = open('input.txt', 'r')
string = file1.read()
list = string.split('\n')

replacements = [
    ('one', '1'),
    ('two', '2'),
    ('three', '3'),
    ('four', '4'),
    ('five', '5'),
    ('six', '6'),
    ('seven', '7'),
    ('eight', '8'),
    ('nine', '9'),
    ('ten', '10')
]

replacementsReversed = [
    ('ten', '10'),
    ('nine', '9'),
    ('eight', '8'),
    ('seven', '7'),
    ('six', '6'),
    ('five', '5'),
    ('four', '4'),
    ('three', '3'),
    ('two', '2'),
    ('one', '1')
]

total = 0

for i in list:
    j = i
    first = ''
    last = ''

    for old, new in replacements:
        i = i.replace(old, new)
    
    for old, new in replacementsReversed:
        j = j.replace(old, new)
   
    for characteri, characterj in itertools.zip_longest(i, j, fillvalue=''):
        if characteri.isdigit() and first == '':
            first = characteri
        elif characterj.isdigit() and first == '':
            first = characterj
        elif characteri.isdigit() and first != '':
            last = characteri
        elif characterj.isdigit() and first != '':
            last = characterj
        else:
            continue

    if (last == '') & (first == ''):
        continue
    elif last == '':
        combined = first + first
        number = int(combined)
        total += number
    else:
        combined = first + last
        number = int(combined)
        total += number
    
print(total)
