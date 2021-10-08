class Person:
    def __init__(self):
        self.name="neeraj"
        self._secret="hi"
p=Person()
print(p.name)
print(p._secret)