lines = [*open(0)]
numbers = map(int, lines[1:])
sorted_numbers = sorted(numbers)
print(*sorted_numbers)