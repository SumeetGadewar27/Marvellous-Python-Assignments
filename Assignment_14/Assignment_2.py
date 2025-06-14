#Write a Class Rectangle with len and with. Adda Method o Compute area and Perimeter 

class Rectangle():
    def __init__(self, Length, Width):
        self.len=Length
        self.wid=Width

    def area(self):
        Area= self.len * self.wid
        print( " Area : ",Area)
    
    def perimeter(self):
        Perimeter = 2 * self.len * self.wid
        print( " Perimeter : ",Perimeter)

def main():

    obj=Rectangle(25,2)
    obj.area()

    obj2=Rectangle(7,2)
    obj2.perimeter()

if __name__ == "__main__":
    print("~"*50)
    main()
        