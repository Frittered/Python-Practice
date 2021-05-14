# Create function with if else user input
def accept_yes(user_input):
    return print('Yes') if user_input.upper() == 'YES' else print('No')
accept_yes(input('Can you type yes?  '))
