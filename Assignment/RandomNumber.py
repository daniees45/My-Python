import random

number = random.randint(1, 10)

high = 0
low = 0
guess = 0
guessNumber = 0


while guess == 0:
        
         userNum = int(input("Guess a number between 1 and 10: "))
         guessNumber += 1
         if userNum < number :
            print ("Too low, Try again")
            low += 1
            
         elif userNum > number :
            print("Too high, Try again")
            high += 1
         else: 
            print(f"Congrats, you guess correctly, Number of guess: {guessNumber}")
            guess += 1
         
            
        
        

