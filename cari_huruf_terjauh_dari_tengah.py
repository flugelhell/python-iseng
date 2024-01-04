import string

alphabet_list = list(string.ascii_uppercase)

def get_huruf_terjauh_dari_tengah(text):
    first = text[0]
    second = text[1]
    third = text[2]

    idx_first = alphabet_list.index(first.upper())
    idx_second = alphabet_list.index(second.upper())
    idx_third = alphabet_list.index(third.upper())

    idx = [idx_first, idx_second, idx_third]
    idx_sorted = sorted(idx)

    left = idx_sorted[1]-idx_sorted[0]
    right = idx_sorted[2]-idx_sorted[1]

    result = left < right
    if result:
        return {'sorted': [alphabet_list[i] for i in idx_sorted],'longest':alphabet_list[idx_sorted[2]]}
    else:
        return {'sorted': [alphabet_list[i] for i in idx_sorted],'longest':alphabet_list[idx_sorted[0]]}

# Main Code
app_start = True
while app_start:
    user_input = input('Enter text with three character: ')

    if user_input == 'exit':
        app_start=False
    elif len(user_input) != 3:
        print('Please input 3 character of text')
    elif any(char.isdigit() for char in user_input):
        print('Please input only alphabet not number')
    elif any(not char.isalnum() for char in user_input):
        print('Please input only alphabet not symbol')
    else:
        res = get_huruf_terjauh_dari_tengah(user_input)
        print(f'The longest character from middle of [{",".join(res.get("sorted"))}] is {res.get("longest")}')
