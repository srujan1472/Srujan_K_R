a = int(input("Enter a number: "))

print("Output:", end=" ")
for i in range(a):
    print(2 * i + 1, end="")
    if i < a - 1:
        print(", ", end="")
print()  
