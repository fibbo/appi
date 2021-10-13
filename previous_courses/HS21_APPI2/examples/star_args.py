def addition(*numbers):
    result = 0
    for n in numbers:
        result += n
    return result


print(addition(4, 5, 6, 7, 3, 123.3))

list_of_numbers = [-4, 5, 3, 12, 10]
print(min(list_of_numbers))

print(min(-4, 2, 23, 3, -23, 3))
