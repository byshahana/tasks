numbers = [10, 45, 23, 89, 67]

largest=(0)
second_largest=(0)
for num in numbers:
    if num>largest:
        second_largest=largest
        largest=num
    elif num>second_largest and num != largest:
        second_largest=num
print("second_largest:",second_largest)