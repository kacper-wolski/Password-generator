from string import ascii_lowercase, ascii_uppercase

# libraries made by me 
import randomizer
import functions

# clear text before starting program to not have anything messy at the start
functions.clear_text()

# lists with characters
numbers = [str(digit) for digit in range(10)]
letters =  list(ascii_lowercase)
uppercase = list(ascii_uppercase)
special_characters = ['!', '@', '#', '$', '%', '^', '&', '*']
number_of_chars = 8

# status of the list - '[ ]' turned off - '[-]' turned on
options_status = {
    'numbers': '[-]',
    'letters': '[-]',
    'uppercase': '[ ]',
    'special characters': '[ ]'
    }

output = ''

# whole program running in a loop
while (True):
    print(f'''To change option, just type it. In order to generate password, type 'generate'
          {options_status['numbers']} Numbers
          {options_status['letters']} Letters
          {options_status["uppercase"]} Uppercase
          {options_status["special characters"]} Special Characters
          {number_of_chars} - Number of characters
          ''')
    print(f'Output: {output}')
    user_input = input('>')
    

    # When user types a function, it is changed either off or on
    if user_input.lower() in options_status:
        status = options_status[user_input.lower()]
        options_status[user_input.lower()] = functions.toggle_option(status)

    elif user_input.lower() == 'generate':
        output = randomizer.random_password(number_of_chars, options_status, numbers, letters, special_characters, uppercase)

    # try is used because user can type something different than an integer, we are preventing program from crashing
    elif user_input.lower() == 'number of characters':
        try:
            number_of_chars2 = input('Enter number of characters: ')
            number_of_chars = int(number_of_chars2)
        except ValueError:
            output = 'Invalid input, enter an integer'

    # typing quit closes the program
    elif user_input.lower() == 'quit':
        break

    else:
        output = 'Error, Wrong command.'

    # at the end, all is being cleared in order to rewrite it with new data, just to not have a bunch of used before text, to make it more user friendly
    functions.clear_text()