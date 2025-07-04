text = input("Enter a string: ")

char_count = {}

for char in text:
    if char in char_count:
        char_count[char] += 1  
    else:
        char_count[char] = 1   

print("Character count:")
for key, value in char_count.items():
    print(f"{key}: {value}")