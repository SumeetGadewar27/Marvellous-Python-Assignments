class circle:
    pi = 3.14
    def __init__(self):
        self.Redius = 0.0
        self.Area = 0.0 
        self.Circumferance = 0.0
    
    def Accept(self):
        self.Redius=int(input("Enter thr radius : "))
        # return self.Radius
    
    def CalculateArea(self):
        self.Area=( circle.pi * (  self.Redius ** 2) )
        # return self.Area
    
    def CalculateCircumferaence(self):
        self.Circumferance =((2 * circle.pi) * self.Redius)
        # return self.Circumferance

    def Dispay(self):
        print("The Radius is ",self.Redius)
        print("The Area is ",self.Area)
        print("The Circumferance is ",self.Circumferance)
     
def main(): 
    obj1=circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumferaence()
    obj1.Dispay()
    
if __name__=="__main__":
    print("~"*50)
    main()