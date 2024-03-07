word = input("Enter a word: ")

reversed = " "

for i in range(len(word) - 1, -1):
    reversed +=  word[i]
print(f"Rversed Word: {reversed}")