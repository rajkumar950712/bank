class bank:
    def __init__(self,amount):
        self.amount=amount
        
    def withdraw(self,wam):
        if wam>self.amount:
            self.amount=self.amount-wam
        else:
            print("emount is not available")
    def deposite(self,dam):
        self.amount=self.amount+dam
    
    def display(self):
        print(self.amount)

if __name__=='__main__':
    account=bank(100)
    while(True):
        print('Welcome to chase bank')
        print('1. Display the amount')
        print('2. add amount')
        print('3. withdrw amount')
        user_choice=int(input())
        if user_choice==1:
            account.display()
        elif user_choice==2:
            am=int(input("please enter amount"))
            account.deposite(am)
        elif user_choice==3:
            am=int(input("please enter amount"))
            account.withdraw(am)
        else:
            exit
            