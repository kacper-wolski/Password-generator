from os import name, system

# function for clearing console
def clear_text():
    if name == 'nt':  # Windows
        system('cls')
    else:
        system('clear') # Other systems (Linux, Mac etc.)


# changes the option to either on or off depending on it's current status
def toggle_option(status):
    return '[-]' if status == '[ ]' else '[ ]'