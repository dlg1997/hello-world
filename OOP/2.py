class studeng():
    name = "dlg"
    age = 21;

print(studeng.__dict__)

cff = studeng()
print(cff.__dict__)
print(cff.name)


class A():
    name = "cff"
    age = 22
    def say(self):
        self.name = "dlg"
        self.age = 21
print(A.name)
print(A.age)

print("*" * 20)

print(id(A.name))
print(id(A.age))

print("*" * 20)

a = A()
print(a.name)
print(a.age)
print("*" * 20)
print(id(a.name))
print(id(a.age))