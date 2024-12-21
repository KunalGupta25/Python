print('''
==========================
    Password Analyzer
==========================
''')

password = input('Enter a Pasword: ')
points = 0
suggestion = []

# Check if the string contais special characters or not
def has_special_chracter(str):
    special_characters = list('!@#$%^&*(){}[]<>?_-.,`~')
    for char in str:
        if char in special_characters:
            return True
    return False
    
uppercase = any(char.isupper() for char in password)
lowercase = any(char.islower() for char in password)
has_num = any(filter(str.isdigit, password))
has_symbols = has_special_chracter(password)



#check Length
if len(password) < 12:
    points -= 2
    suggestion.append('Suggestion: Increase the Length of the Password!')
elif len(password) > 12 and len(password) < 15:
    points += 2
else:
    points += 3

#check it it contains Uppercase Letters
if uppercase:
    points += 2
else: 
    suggestion.append('Suggestion: You Should add Uppercase Letters to improve password strength')

# Check if contain Lowercase Letters
if lowercase:
    points += 2
else:
    suggestion.append('Suggestion: You Should add Lowercase Letters to improve password strength')

# Check if contains Numbers
if has_num:
    points += 2
else: 
    suggestion.append('Suggestion: You Should add Numbers to improve password strength')

# Check if contains symbols
if has_symbols:
    points += 2
else:
    suggestion.append('Suggestion: You Should add Symbols to improve password strength')


def grade(points):
    if points >= 8:
        return 'Strong'
    elif points >= 5:
        return 'Moderate'
    elif points >= 3:
        return 'weak'
    else:
        return 'superweak'


if __name__ == '__main__':
    print(f'Overall Score: {points}\nRank: {grade(points)}')
    for str in suggestion:
        print(f'- {str}')
