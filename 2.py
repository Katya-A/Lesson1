umber = []
for number in range(1, 1001, 2):
    number = number ** 3
    print(number)

    sum_digit = 0
    while number > 0:
        last_digit = number % 10
        sum_digit += last_digit
        number = number // 10
        print(last_digit)  # разделение по 1 цифре

    if sum_digit % 7 == 0:
        print(sum_digit)
umber2 = []  # последовательность + 17
for number in range(1, 1001, 2):
    number = number ** 3
    number += 17
    print(number)  # кубы +17

    sum_digit2 = 0
    while number > 0:
        last_digit = number % 10
        sum_digit2 += last_digit
        number = number // 10
        print(last_digit)  # разделение по 1 цифре

    if sum_digit2 % 7 == 0:
        print(sum_digit2)
