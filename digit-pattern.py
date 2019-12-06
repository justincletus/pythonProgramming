def pattern(n):
    for i in n:
        print("|", end="")

        if n.find(i):
            print('hi')

        print("*" * int(i))


n = "41235"
pattern(n)
