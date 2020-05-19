"""
Base case:
if num // 10 ==0:
    return total + num %10
else:
    total = total + num %10
    num = num //10


"""

def sum_of_digit(num,total):
    if num // 10 == 0:
        return total + num % 10
    else:
        total = total + num % 10
        num = num // 10
        return sum_of_digit(num,total)


def sum_of_digit_1(num,total):
    if num == 0:
        return total
    else:
        total = total + num % 10
        num = num // 10
        return sum_of_digit_1(num,total)

print(sum_of_digit(1,0))


