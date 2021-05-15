class Fases():
    """Класс, который будет определять грань многогранника"""
    def __init__(self, a,b,c):
        self.a = a
        self.b = b
        self.c = c
    def cf(self, i):
        if (i==0):
            return self.a
        elif (i==1):
            return  self.b
        elif (i==2):
            return self.c
    def __index__(self):
        return print('hello')


class Changeable:
    def __init__(self, color):
        self.color = color

    def __call__(self, newcolor):
        self.color = newcolor

    def __str__(self): # Метод, который возвращает строку
        return "%s" % self.color


class fases(object):

    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c
        self.storage = {}

    def __setitem__(self, key, value):
        self.storage[key] = value
    def __getitem__(self, key):
        if (key == 0):
            return  self.a
        elif (key == 1):
            return  self.b
        elif (key == 2):
            return  self.c
        else:
            return None