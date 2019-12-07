def fab(n):
    if n < 0:
        print("Incorrect number")
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fab(n-1)+fab(n-2)

print(fab(8))
