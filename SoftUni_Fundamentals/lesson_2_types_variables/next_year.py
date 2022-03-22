def next_happy_counter(year):
    is_happy_year = False

    while not is_happy_year:
        year += 1
        str_year = str(year)
        set_year = set(str_year)
        is_happy_year = len(str_year) == len(set_year)
    return year


start_year = int(input())
print(next_happy_counter(start_year))
