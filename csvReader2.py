import csv
with open('test.csv', 'rU') as csv_file:
    filtered = (line.replace('\r', '') for line in csv_file)
    for row in csv.reader(filtered):
        print(row)

#     sample = csv_file.read(64)
#     has_header = csv.Sniffer().has_header(sample)
#     print(has_header)
#
#     deduced_dialect = csv.Sniffer().sniff(sample)
#
# with open('test.csv', 'r') as csv_file:
#     objects = csv.reader(csv_file, deduced_dialect)
#
#     for obj in objects:
#         print(obj)