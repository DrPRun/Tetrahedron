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
        else:
            return self.c