
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

def expense(balance,transaction_no,transaction,balance_amt):
   reason=input("Enter the reason : ")
   expense_amt=int(input("Enter the amount :"))
   transaction_no=transaction_no+1
   exp_row=[transaction_no,reason,expense_amt]
   transaction.append(exp_row)
   return transaction,balance_amt
	
def income(balance,transaction_no,transaction,balance_amt):
   reason=input("Enter the reason :  ")
   income_amt=int(input("Enter the amount :"))
   transaction_no=transaction_no+1
   income_row=[transaction_no,reason,income_amt]
   transaction.append(income_row)
   return transaction,balance_amt

def statement(transaction,balance_amt):
   print(transaction)
   print("Balance :",balance_amt)
	
def usr_exit():
   print("----exit---")

if __name__=="__main__":
   transaction_no=0
   transaction=[]
   choice=0
   first_name=input("First name : ")
   last_name=input("Last name : ")
   initial_amount=int(input("Your initial amount : "))
   balance_amt=initial_amount   
   while choice!=4:
      choice=showchoice()
      opt(choice,initial_amount,transaction_no,balance_amt)
    
 
