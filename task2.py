class MyList:

    def __init__(self):
        self.a = [2, 3, 7, 4, 9]
        self.b = 10
        self.c = []

    def get_missing(self):
        for i in range(1, self.b+1):
            if i in self.a:
                continue
            else:
                self.c.append(i)

MyNewList = MyList()

MyNewList.get_missing()

print(MyNewList.c)