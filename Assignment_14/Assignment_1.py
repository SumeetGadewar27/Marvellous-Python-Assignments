class Person():
    def __init__(self, Name, Age):
        self.Name = Name
        self.Age=Age
    def Diplay(self):
        print(self.Name, self.Age) 

class Teacher(Person):
    def __init__(self, Name, Age, Subject, Salary):
        super().__init__(Name, Age)
        self.Subject = Subject
        self.Salary = Salary

    def Display(self):
        print(self.Name, self.Age, self.Subject , self.Salary)

def main():
    Sobj=Person("Ravi",28)
    print(Sobj.Diplay())

    obj=Teacher("Sumeet",29,"Marathi",10000)
    print(obj.Display())

if __name__ == "__main__":
    print("~"*50)
    main()
        