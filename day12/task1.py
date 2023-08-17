# first 50 even numbers

n = 0
even_count = 0
while even_count != 50:
    if n % 2 == 0:
        print(n)
        even_count += 1
    n += 1
