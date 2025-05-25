import multiprocessing as mp
import os 
listB=[]
def Factor(ListA):
    A=1
    print("This PID : ",os.getpid())
    for j in range(1,ListA+1):
        A=A*j
        
    return A

def main():
    ListA=[5,6,12,5,6,12,5,6,12,5,6,12]
    listB=[]

    MultiCore=mp.Pool()
    MultiCore1=MultiCore.map(Factor,ListA)
    print(MultiCore1)
    MultiCore.close()
    # MultiCore.start()



if __name__ == "__main__":
    print("~"*50)
    main()