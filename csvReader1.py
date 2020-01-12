
with open('test.csv', 'r') as f:
    lines = [line.rstrip() for line in f]


    objects = []
    for line in lines:
        
        words = line.split(',')
        objects.append((words[0], words[1:]))

    for obj in objects:
        print(obj)
