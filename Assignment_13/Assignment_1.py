class BookStore():
    NoOfBooks = 0
    def __init__(self,A ,B):
        self.Name=A
        self.Author=B
    
    def Display(self):
        BookStore.NoOfBooks=BookStore.NoOfBooks+1
        print(self.Name, " by ",self.Author ,". No of Books : " ,BookStore.NoOfBooks)
        

def main():

    obj1=BookStore("Linux System Programming","Robert Love")
    obj1.Display()

    obj1=BookStore("C Programming ","Dennis Ritchie")
    obj1.Display()

if __name__ == "__main__":
    print("~"*50)
    main()


        