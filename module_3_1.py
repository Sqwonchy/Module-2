calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    str_1 = len(string)
    str_2 = string.lower()
    str_3 = string.upper()
    str_ = (str_1,str_2,str_3)
    return str_

def is_contains(string: str, list_to_search: list):
    count_calls()
    list_ = string.lower()
    list_search = []
    for word in list_to_search:
        m = word.lower()
        list_search.append(m)
    search_ =set(list_search)
    return  list_ in search_




print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)

