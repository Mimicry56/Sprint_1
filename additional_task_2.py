def digit_root(num):
    if num <= 9:
        return num
    else:
        sum_of_digits = 0
        for digit in str(num):
            sum_of_digits += int(digit)
        return digit_root(sum_of_digits)