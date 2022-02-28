def verify_password(string):
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+']
    count = 0
    requirements = {'lower': False, 'upper': False, 'special': False, 'number': False}

    for i in string:
        if i.lower() == i:
            requirements['lower'] = True
        if i.upper() == i:
            requirements['upper'] = True
        if i in special_characters:
            requirements['special'] = True
        if i.isnumeric() == True:
            requirements['number'] = True

    for key, value in requirements.items():
        if value == True:
            count += 1
    
    if len(string) < 6 and count == 4:
        return 6 - len(string)
    elif len(string) >= 6 and count < 4:
        return 4 - count
    elif len(string) <= 3 and count < 4:
        return 6 - len(string)
    elif len(string) == 4 and count == 3:
        return  6 - len(string)
    elif len(string) >= 4 and count < 4:
        return 4 - count
    else:
        return 0
    

print(verify_password('Ya3'))
