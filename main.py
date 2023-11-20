def get_word(number):
    if number % 3 == 0 and number % 5 == 0:
        return "VINCLE"
    elif number % 3 == 0:
        return "VIN"
    elif number % 5 == 0:
        return "CLE"
    else:
        return number

result = [get_word(i) for i in range(1, 101)]
print(result)
