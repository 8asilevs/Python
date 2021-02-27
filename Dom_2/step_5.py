rating = [7, 5, 3, 3, 2]

new_number = int(input('Введите число'))

if new_number > rating[0]:
    rating.insert(0, new_number)

if new_number < rating[len(rating)-1]:
    rating.insert(len(rating), new_number)

i = 0
max = len(rating)

while i < max:
    if new_number == rating[i]:
        rating.insert(i+1, new_number)
        i = max
    elif (new_number < rating[i] and new_number > rating[i+1]):
        rating.insert(i+1, new_number)
        i = max
    i += 1

print(rating)