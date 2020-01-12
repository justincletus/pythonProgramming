import csv

# created csv format function before extracting data
def simple_csvformat(data):
    result = []
    for i, a in enumerate(data):
        if i + 1 != len(data) and data[i+1][0] == ',':
            a = a.replace('\n', '')
            result.append(a + data[i + 1])
        elif a[0] != ',':
            result.append(a)
    return result

# attached file encoded type if the file not encoded using UTF-8
data = [line for line in open('test2.csv', 'r', encoding='ISO-8859-1')]
sdata = simple_csvformat(data)

with open('out2.csv', 'w') as f:
    for row in sdata:
        f.write(row)

result = [list(val.replace('\n', '') for val in line) for line in csv.reader(open('out2.csv', 'r'))]

with open('out2.csv') as infile:
    csv.register_dialect('strip', skipinitialspace=True)
    objects = csv.DictReader(infile, dialect='strip')
    fieldname = objects.fieldnames

    for obj in objects:
        print(obj['entrydate'])
