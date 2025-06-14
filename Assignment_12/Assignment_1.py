class Demo():
    Value=1 #Class veriable
    def __init__(self,no1,no2): # instance Method 
        self.val1=no1  #in
        self.val2=no2
    
    def fun(self): #instance method
        print("Fun - ",self.val1," Val1 ",self.val2," Val2 ")
    def gun(self): #instance Method
        print("Gun - ",self.val1," Val1 ",self.val2," Val2 ")


def main():
    obj1=Demo(11,21)
    obj2=Demo(51,101)

    obj1.fun()
    obj1.gun()
    obj2.fun()
    obj2.gun()



if __name__ == "__main__":
    print("~"*50)
    main()