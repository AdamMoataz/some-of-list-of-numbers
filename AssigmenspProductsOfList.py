numbers = [1,2,3,4,6,7,8]
# Write a program to find the product of the list of numbers using while loop

product = 1

# product = numbers[0] * numbers[1] * numbers[2] * numbers[3] * numbers[4] * numbers[5] * numbers[6] 


#OMG IT PRINTED NORMALLY

for i in range(len(numbers)):
    product = product*numbers[i]

print(product)