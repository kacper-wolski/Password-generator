def random_password(number_of_chars, options_status, numbers, letters, special_characters, uppercase):
    from random import choices
    user_list = []
        
    # checks if every option is on. If it is, it will be used. If not, it won't be included
    if options_status['letters'] == '[-]':
        user_list += letters

    if options_status['special characters'] == '[-]':
        user_list += special_characters

    if options_status['uppercase'] == '[-]':
        user_list += uppercase

    if options_status['numbers'] == '[-]':
        user_list += numbers

    # if list is empty because user didn't selected any option, it prevents from error. otherwise it just returns random password
    if not user_list:
        return 'No character types selected.'
    else:
        return ''.join(choices(user_list, k=number_of_chars))