def am_I_afraid(day,num):
    switcher = {
        'Monday': num == 12,
        'Tuesday': num > 95,
        'Wednesday': num == 34,
        'Thursday': num == 0,
        'Friday': num % 2 == 0,
        'Saturday': num == 56,
        'Sunday': num in [666, -666]
    }
    return switcher.get(day)

print(am_I_afraid('Monday', 15))