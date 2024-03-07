
def Shares():
    NS = int(input("Enter the number of shares: "))
    return NS
def Purchase():
    PP = float(input("Enter the purchase price per share: "))
    return PP 
def Commission():
    PC = float(input("Enter purchase commission paid: "))
    return PC
def SalePrice():
    SP = float(input("Enter the sale price per share: "))
    return SP
def SalesCom():
    SC = float(input("Enter sales commission paid: "))
    return SC
def profit():
    profit = ((Shares() * SalePrice()) - SalesCom()) - ((Shares() * Purchase()) + Commission())
    if profit > 0:
        print(f"The profit is {profit} ")
    else:
        print(f"The loss is {profit}")

profit()