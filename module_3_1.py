calls = 0
def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()
    print((len(string), string.upper(), string.lower()))

def is_contains(string, list_to_search):
    print('Совпадение строк: ', string.upper() in [word.upper() for word in list_to_search])
    count_calls()

string_info('Привет, Мир!!!')
string_info('Мама мыла раму')
is_contains('Мама', ['мама', 'мыла', 'раму'])
is_contains('Мама', ['Привет', 'Мир'])

print('Количество вызовов функций:', calls)