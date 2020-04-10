class Operations:
    def __init__(self):
        self.d1=0
        self.d2=0
    def read(self):
        self.d1 = float(input("Enter the first distance (in metres):"))
        self.d2 = float(input("Enter the second distance (in metres):"))
    def display(self):
        print("The first distance is",self.d1)
        print("The second distance is",self.d2)
    def addDistance(self):
        sum = self.d1+self.d2
        return sum
    def subtractDistance(self):
        sub = max(self.d1,self.d2)-min(self.d1,self.d2)
        return sub
O = Operations()
while(True):
    n=int(input("\nSelect the option to perform the operation:\n1. Read the Distances\n2. Display the distances\n3. Add the Distances\n4. Subtract the distances\n5. Exit \n"))
    if n==5:
        break
    elif n==1:
        O.read()
    elif n==2:
        O.display()
    elif n==3:
        Dist_sum = O.addDistance()
        print("The sum of Distances given is",Dist_sum)
    elif n==4:
        Dist_sub = O.subtractDistance()
        print("The sum of Distances given is",Dist_sub)
    else:
        print("Give valid Input!")

        

    