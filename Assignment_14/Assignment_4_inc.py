#Write a Class Rectangle with len and with. Adda Method o Compute area and Perimeter 

class Student():
    school_name = "Dr D Y Patil School of Engineering, Pune"
    def __init__(self, Name, Roll_no,):
        self.Name = Name
        self.Roll_no = Roll_no

    def Display(self):
        print("Name :",self.Name)
        print("Roll_no :",self.Roll_no)
        print("Collage Name :",Student.school_name)

class Name(Student):
    Student.school_name = "Dr D Y Patil Collage of Engineering, Pune"
    def __init__(self, Name, Roll_no):
        super().__init__(Name, Roll_no)

    def Display(self):
        print("Name :",self.Name)
        print("Roll_no :",self.Roll_no)
        print("Collage Name :",Name.school_name)

def main():
    Sobj=Student("Sumeet",21)
    Sobj.Display() 
    print("- "*28)
    Nobj=Name("Sham",23)
    Nobj.Display()    


if __name__ == "__main__":
    print("~"*50)
    main()
        