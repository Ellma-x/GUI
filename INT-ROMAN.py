class Numeric:

    def __init__(self):

        self.roman = {"1":"I", "2":"II", "3":"III", "4": "IV", "5":"V", "6":"VI", "7":"VII", "8":"VIII", "9":"IX", "10":"X"}

    def us(self):

     while True:
        
        self.user = input("Enter the integer number:")

        if  self.user in self.roman:
            print("Roman numeric is:", self.roman[self.user])

        else:
            print("Sorry! Try again")

        option = input("Do you want to keep going?:(Y/N):")

        if option == "N":
            print("Thank you")
            break
        else:
            Numeric()

obj = Numeric()
obj.us()
            

     
        
