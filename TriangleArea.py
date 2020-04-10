class triangle:
    def __init__(self):
        self.a = 0
        self.b = 0
        self.c = 0
    def getSides(self):
        self.a=int(input("Enter the 1st side:"))
        self.b=int(input("Enter the 2nd side:"))
        self.c=int(input("Enter the 3rd side:"))
    def displayArea(self):
        s = (self.a+self.b+self.c)/2
        area = (s*(s-self.a)*(s-self.b)*(s-self.c))**(0.5)
        print (area)
t = triangle()
t.getSides()
t.displayArea()