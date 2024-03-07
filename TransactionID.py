import random
# Generate a random 6-digit number
random_suffix = ''.join(str(random.randint(0, 9)) for _ in range(5))

# Combine the prefix "202301" with the random suffix
 random_number = f"202402{random_suffix}"
 
print(random_number)
