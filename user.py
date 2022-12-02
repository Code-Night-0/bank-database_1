class User():
    def __init__(self, id: int = 0, name="", surname="asd",email="", password="",balance: int = 0):
        self.id = id
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password
        self.balance = balance

    def withdraw(self):
        try:
            amount = int(input("How much do you want to withdraw? : "))
            if amount > 0:
                if amount < self.balance:
                    self.balance += amount
                    print(f"You have withdrawn {amount}, Your new balance is {self.balance}") 
                else:
                    print("You don't have enough money")
            else:
                print("You can't withdraw negative value")
        except:
            print("Please enter a valid amount.")
    
    def deposit(self, amount):
        try:
            amount = int(input("How much do you want to deposit? : "))
            if amount > 0:
                self.balance -= amount
                print("You have successfully withdrawn : ", amount, f"Your new balance is {self.balance}")
            else:
                print("You can't withdraw negative value")
        except:
            print("You can't deposit negative value")
    
    def changeValue(self):
        changable = str(input("what do you want to change?: "))
        changable = changable.lower()
        if changable in ["name", "surname", "email", "password"]:
            match changable:
                case "name":
                    self.name = input("What is your new name? : ")
                    print(f"You've sucsesfully changed your name. New name is: {self.name}")
                case "surname":
                    self.surname = input("What is your new surname? : ")
                    print(f"You've sucsesfully changed your surname. New surname is: {self.surname}")
                case "email":
                    self.email = input("What is your new email? : ")
                    print(f"You've sucsesfully changed your email. New email is: {self.email}")
                case "password":
                    self.password = input("What is your new password? : ")
                    print(f"You've sucsesfully changed your password. New password is: {self.password}") 
        else:
            print("Please enter a valid value")






    
        
    
    
    
    
#kaan = User(1, "Kaan", "Ayyıldız", "kaan.ayldz@gmail.com", "123321", 100)
#kaan.changeValue()



