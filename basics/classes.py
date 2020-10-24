 #!/usr/bin/python3
__author__ = 'Anon0nyx'

class person:
    def __init__(self, foo):
        self.name = foo

    def get_name(self):
        return self.name

me = person('Dylan Forkey')
x = me.get_name()
print(x)

secondPerson = person('Logan Forkey')
x = secondPerson.get_name()
print(x)
