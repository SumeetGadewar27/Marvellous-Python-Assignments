class Arimetic:
    def __init__(self): # Constructor
        self.Value1=0 # instance Veriable
        self.Value2=0
    
    def Accept(self):  #instance methods
        self.Value1=int(input("Enter 1st Value: ")) 
        self.Value2=int(input("Enter 2nd Value: ")) 

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        return self.Value1 % self.Value2
        
def main(): 
    objA=Arimetic()
    objA.Accept()
    print("Addition of two number",objA.Addition())
    print("Substraction of two number",objA.Substraction())
    
    objB=Arimetic()
    objB.Accept()
    print("Multiplication of two number",objB.Multiplication())
    print("Division of two number",objB.Division())
    
if __name__=="__main__":
    print("~"*50)
    main()