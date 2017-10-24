

class A1:
    def __init__(self,a):
        self.a =a;

    def geta(self):
        print(self.a)

# a = a1("abc");
# a.geta()

class B1(A1):
    def mm(self):
        print("self.a=",self.a)

    def geta(self):
        if self.a == 'aa':
            print("(aa)B1.geta = ",self.a)
        elif self.a == 'bb':
            print("(bb)B1.geta = ",self.a)
        else:
            print("---end--")

nn = B1("aa")
nn.geta()