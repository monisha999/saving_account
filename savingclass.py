class saving_account():
    def __init__ (self,first,last,initial):
        self.first_name = first 
        self.last_name = last
        self.initial_amount = initial

    def showchoice():
        print("1.Expense")
        print("2.Income")
        print("3.Statement")
        print("4.Exit")
        usr_choice=int(input("Enter the choice :"))
        return usr_choice
		
    def opt(choice,balance,transaction_no,balance_amt):
        if choice==1:expense(balance,transaction_no,transaction,balance_amt)
        if choice==2:income(balance,transaction_no,transaction,balance_amt)
        if choice==3:statement(transaction,balance_amt)
        if choice==4:usr_exit()
	

if __name__=="__main__":
    test=saving_account("firstname","lastname",5000)
    print(test.first_name)
