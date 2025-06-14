class BankAccount():
    ROI = 10.5
    def __init__(self):
        self.Name=""
        self.Amount=0

    def Deposite(self):
        self.Name=input("Enter the Name: ")
        self.Amount=int(input("Enter the Deposite Amount: ") )

    def Withdraw(self):
        WAmount=int(input("Enter the Amount to Withdraw "))
        self.Amount=self.Amount - WAmount

    def Bank():
        return "State bank of india"
    
    def CalculateIntrest(self):
        Intrest = 0
        # Year=1
        Intrest = (self.Amount / 100 ) * BankAccount.ROI            #for One Year
        # Intrest = (self.Amount  * BankAccount.ROI * Year )/ 100   #for Specific year like 2,3,4

        self.Amount= self.Amount+Intrest
        print("Intrest is : ", Intrest)
    
    def Display(self):
        print("Bank Name ",BankAccount.Bank(),"| Name of Account Holder: ",self.Name,  "|  Balance Amount: " , self.Amount )


def main():

    obj1=BankAccount()
    obj1.Deposite()
    obj1.Withdraw()
    obj1.CalculateIntrest()
    obj1.Display()

if __name__ == "__main__":
    print("~"*50)
    main()


        