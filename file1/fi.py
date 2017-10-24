

def mm():
    with open("a.txt") as f:
        contend = f.read();
        print(contend)


def write():
    with open("a.txt","w") as w:
        w.write("aa")

def append():
    with open("a.txt","a") as ap:
        ap.write("\nbb")


write()
append()
mm()