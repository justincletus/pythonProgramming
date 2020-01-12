import csv

with open('test.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column name are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} \t{row[1]} \t{row[2]} \t{row[4]} \t{row[5]} \t{row[6]} \t{row[7]} \t{row[8]} \t{row[9]} ')
            line_count += 1
    print(f'Processed {line_count} lines')