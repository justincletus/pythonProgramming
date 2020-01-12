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

data = [line for line in open('test.csv', 'r')]
sdata = simple_csvformat(data)

with open('out.csv', 'w') as f:
    for row in sdata:
        f.write(row)

result = [list(val.replace('\n', '') for val in line) for line in csv.reader(open('out.csv', 'r'))]

with open('out.csv') as infile:
    csv.register_dialect('strip', skipinitialspace=True)
    objects = csv.DictReader(infile, dialect='strip')
    fieldname = objects.fieldnames

    for obj in objects:
        print(obj['year'])
