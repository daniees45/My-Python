def menu():
    print("1. Transfer\n"+
          "2.Airtime\n"+
          "3.Exit")
    

def choice():
    choice = int(input("choice:"))
    return choice
def check(): 
    ussd = input("Enter the shortcode: ")
    if ussd == "*170#":
        menu()
    else:
        print("Invalid Code")
def Network():
    print("1.MTN\n"+
          "2.Vodafone")

def checkMenu():
    if choice() == 1:
        Network()
    elif choice() == 2:
        print("Vodafone")
def MobileMoney():
    check()
    checkMenu()

MobileMoney()