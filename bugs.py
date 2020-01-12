"""very buggy hello world program ...
please fix anything you see that looks "wrong"
"""

# initialization
str = None
var = None


def setvar(val):
    var = val.strip()  # we want the leading and trailing spaces removed
    if var in val:
        if val:
            print("setting variable {var} in", val)
        print(var)
    return var


if __name__ == "__main__":
    try:
        setvar(" hello world! ")  # use this function to set the 'var' variable
    except:
        print("something went wrong")
