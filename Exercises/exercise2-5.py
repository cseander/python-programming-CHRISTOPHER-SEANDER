sum, counter, n = 1.0, 1.0, input("Enter value for n: ") 

while counter <= int(n):
    sum += 1.0 / (2.0 ** counter)
    counter += 1.0

print(sum)

sum2, counter2, n2 = 1.0, 1.0, input("Enter value for n: ")

while counter2 <= int(n2):
    sum2 += ((-1) ** counter2) / ((2 * counter2) + 1)
    counter2 += 1.0

print(sum2)