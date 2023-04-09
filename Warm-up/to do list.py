user_input = 'random'
data = []

def show_menu():
    print('Menu:')
    print('1. Add an item')
    print('2. mark as done')
    print('3. view to do items')
    print('4. exit')

while user_input != '4':
    
    show_menu()
    user_input = input('enter your choice: >>>')
    if user_input == '1':
        item = input('What is to be done? >>>')
        data.append(item)
        print('Added item:', item)
    elif user_input == '2':
        item = input('What is to be mark as done? >>>')
        if item in data:
            data.remove(item)
            print('removed item: ',item)
        else:
            print('the item does not exist in the list!')
    elif user_input == '3':
        print('list of to do items:')
        for item in data:
            print(item)
    elif user_input == '4':
        print('GoodBye')
    else:
        print('please enter either 1, 2, 3, or 4')

