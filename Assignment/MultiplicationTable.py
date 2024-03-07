num = int(input("Enter a number to multiply: "))

print(f"Multiplication Table for {num}\n")
for i in range(11):
    print(f"{num} * {i} = {num * i}\n")