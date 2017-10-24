
def e1():
    try:
        print(2/0)
    except:
        print("zero erro")
    else:
        print("end")

# e1()

def fe():
    try:
        with open("mm.txt") as mm:
            conten = mm.read()
    except FileNotFoundError:
        print("file not exist")

fe()

