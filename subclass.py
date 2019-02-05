class Super():
    def __init__(self, name):
        self.name = name

    def sayHi(self):
        print("hi, ", self.name)

    def sayBye(self):
        print(f"goodbye, {self.name}")


class Sub(Super):
    def __init__(self):
        super().__init__('foo')
        self.name = 'bar'

    def sayHello(self):
        print(f"hello, {self.name}")
        self.sayBye()


my = Sub()

my.sayHi()

my.sayHello()
