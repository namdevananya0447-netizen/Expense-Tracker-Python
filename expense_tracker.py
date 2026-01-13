def add_expense(expense):
    
   
    while True:
        try:
            amount=int(input("enter amount(enter 0 to stop):"))
            if amount<0:
                print("Enter a valid amount")
                continue
            if amount==0:
                break
            category=input("enter the expense category:")
            description=input("any additional detail you wish to add:")
            data={}
            data["amount"]=amount
            data["category"]=category
            data["description"]=description
            expense.append(data)
        except ValueError:
            print("enter valid data")
def show_expense(expense):
    if not expense:
        print("No expense added yet")
        return
    for x in expense:
        print(f"Expense {x}")
        print("amount spent:",x.get("amount"))
        print("category of expenditure:",x.get("category"))
        print("additional note:",x.get("description"))
        print("--------------------------------------------------------------------------------------------------------------------------")
def total_expense(expense):
    
    total=0
    for x in expense:
        amount=x.get("amount")
        total+=amount
    print("Total expense:",total)
    que=input("Enter yes if you want to see where you spent the most(yes/no)?")
    if que=="yes":
        max_expense=max(expense,key=lambda x:x.get("amount"))
        print("Amount:",max_expense.get("amount"))
        print("Category:",max_expense.get("category"))
expense=[]

while True:
    try:
        print("1.Add expense")
        print("2.show expenses")
        print("3.show total expense")
        print("4.Exit")
        
        choice=int(input("enter your choice:"))
        if choice==1:
            add_expense(expense)
        elif choice==2:
            show_expense(expense)
        elif choice==3:
            total_expense(expense)
        elif choice==4:
            print("exiting......")
            break
    except ValueError:
            print("enter a valid choice")
